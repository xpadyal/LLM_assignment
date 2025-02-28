
    const welcomeText = "Welcome to Deepscribe Helper. How can I assist you today?";
    const welcomeElem = document.getElementById("welcome-message");
    let charIndex = 0;
    function typeWriter() {
      if (charIndex < welcomeText.length) {
        welcomeElem.innerHTML += welcomeText.charAt(charIndex);
        charIndex++;
        setTimeout(typeWriter, 50);
      }
    }
    window.onload = typeWriter;

    // Global conversation array
    let conversation = [];

    let transcript = '';
    let soapNote = '';

    // Fetch the transcript and SOAP note.
    async function fetchNotes() {
        try {
            const response = await fetch('/notes');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            
            if (data.transcript) {
                transcript = data.transcript;
            } else {
                console.error('Transcript data is missing in the API response');
            }
    
            soapNote = data.soap_note || '';
        } catch (error) {
            console.error('Failed to fetch notes:', error);
        }
    }

    // Call the fetchNotes function when the window loads
    window.onload = async function() {
        await fetchNotes();
        typeWriter(); 
    };

    // Function to highlight words wrapped with asterisks
    function highlightText(message) {
        return message.replace(/\*\*(.*?)\*\*/g, '<span class="highlight" onclick="showDetails(\'$1\')">$1</span>');
    }

    // Function to show details (Transcript or SOAP notes)
    function showDetails(term) {
    
        // Normalize the term: trim whitespace, convert to lowercase
        const normalizedTerm = term.trim().toLowerCase();
    
        // Normalize transcript and SOAP note
        const normalizedTranscript = transcript.toLowerCase();
        const normalizedSoapNote = soapNote.toLowerCase();
    
        // Split the term into individual words and filter out common stop words
        const stopWords = new Set(['not','the', 'and', 'is', 'in', 'it', 'to', 'of', 'for', 'with', 'on', 'at', 'by', 'this', 'that', 'have', 'has', 'had']);
        const words = normalizedTerm.split(/\s+/).filter(word => !stopWords.has(word));
        console.log('Words to search for:', words);
    
        // Highlight words in the transcript
        const highlightedTranscript = words.reduce((acc, word) => {
            const regex = new RegExp(`(\\b${word.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\b)`, 'gi'); // Use word boundaries
            return acc.replace(regex, '<span class="highlight">$1</span>'); // Highlight the word
        }, normalizedTranscript);
    
        // Highlight words in the SOAP note
        const highlightedSoapNote = words.reduce((acc, word) => {
            const regex = new RegExp(`(\\b${word.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\b)`, 'gi'); // Use word boundaries
            return acc.replace(regex, '<span class="highlight">$1</span>'); // Highlight the word
        }, normalizedSoapNote);
    
        // Check if ALL words are present in the transcript or SOAP note
        const allWordsInTranscript = words.every(word => normalizedTranscript.includes(word));
        const allWordsInSoapNote = words.every(word => normalizedSoapNote.includes(word));
    
        let details = '';
    
        if (allWordsInTranscript) {
            details = `Transcript: ${highlightedTranscript}`;
            
        } else if (allWordsInSoapNote) {
            details = `SOAP Note: ${highlightedSoapNote}`;
        
        } else {
            details = 'No details found.';
        
        }

        // Set the modal body content
        document.getElementById('modal-body').innerHTML = details;

        // Show the modal
        const modal = document.getElementById('notes-modal');
        modal.style.display = "block";

        // Close the modal
        const closeButton = document.querySelector('.close-button');
        closeButton.onclick = function() {
            modal.style.display = "none";
        }

        // Close the modal when the user clicks anywhere outside of the modal
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    }

    // Append message to the chat window with highlighting
    function appendMessage(message, isUser) {
        // Create a wrapper for the message
        const messageWrapper = document.createElement("div");
        messageWrapper.className = "message-wrapper " + (isUser ? "user" : "assistant");

        const messageElem = document.createElement("div");
        messageElem.className = "message " + (isUser ? "user" : "assistant");

        messageElem.innerHTML = highlightText(message); // Use highlightText to format the message

        // Append the message element to the wrapper
        messageWrapper.appendChild(messageElem);
        document.getElementById("chat-window").appendChild(messageWrapper);

        // Auto-scroll to the bottom
        document.getElementById("chat-window").scrollTop = document.getElementById("chat-window").scrollHeight;
    }

    // Send message to the API
    async function sendMessage() {
      const input = document.getElementById('userInput');
      const message = input.value.trim();
      
      if (!message) return;
      
      // Clear the input and append the user's message
      input.value = '';
      appendMessage(message, true);
      conversation.push({ role: 'user', content: message });
    
      try {
          const response = await fetch('/ask/invoke', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                  input: conversation  // Wrap the conversation list in an "input" field
              })
          });
          
          const data = await response.json();
          console.log("Response Data:", data);
          
          if (data.error) {
              appendMessage(`Error: ${data.error}`, false);
          } else {
            const answer = data.output?.output?.content;
              console.log(answer);
              appendMessage(answer, false);
              conversation.push({ role: 'assistant', content: answer });
          }
      } catch (error) {
          appendMessage('Failed to get response. Please check your connection.', false);
      }
    }
    
    document.getElementById("send-button").addEventListener("click", sendMessage);
    
    // Allow sending message by pressing Enter.
    document.getElementById("userInput").addEventListener("keypress", function(e) {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
      }
    });