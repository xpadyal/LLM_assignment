transcript = """
Provider: Good morning, how are you feeling today?

Patient: Not too great. I've had this persistent cough and fever for about a week now.

Provider: I’m sorry to hear that. Have the symptoms been getting worse over time?

Patient: Yes, the fever started around five days ago, and it hasn't gone away. The cough has been persistent, and my throat is really sore. I also feel exhausted all the time.

Provider: Have you noticed any other symptoms, such as shortness of breath, chest pain, or headaches?

Patient: No chest pain, but I have had some mild headaches, and my nose has been stuffy. Breathing feels a little difficult, but it's not too bad.

Provider: Have you been taking anything for the fever or other symptoms?

Patient: Just ibuprofen every few hours, but it doesn't seem to help much. I also tried drinking warm tea with honey for my throat, but it still hurts.

Provider: Have you had any chills, night sweats, or body aches?

Patient: Yes, chills and body aches started about three days ago. I wake up sweating at night.

Provider: Have you had any nausea, vomiting, or diarrhea?

Patient: No vomiting or diarrhea, but I have felt nauseous a couple of times, especially when I wake up.

Provider: Have you had any recent exposure to someone who was sick?

Patient: My coworker was sick about a week ago. He had a bad cold and a cough. I sit pretty close to him in the office.

Provider: Have you had any difficulty swallowing or changes in appetite?

Patient: Swallowing is painful, and I haven't had much of an appetite. I mostly eat soup and soft foods.

Provider: Have you experienced any dizziness or lightheadedness?

Patient: Yes, sometimes when I stand up quickly.

Provider: Any history of asthma, allergies, or chronic respiratory conditions?

Patient: No, I don’t have any chronic conditions.

Provider: Do you smoke or have a history of smoking?

Patient: No, I don’t smoke.

Provider: Have you been drinking enough fluids?

Patient: I try to, but my throat hurts, so I probably haven’t been drinking as much as I should.

Provider: Have you been able to get enough rest?

Patient: Not really. The coughing keeps me up at night, and I feel very tired throughout the day.

Provider: Let me check your vitals. Your temperature is 102°F, and your oxygen saturation is 97%. Your throat is red with some white patches on the tonsils. Your lungs sound clear, but there is mild congestion in your nasal passages.

Patient: So, what do you think it is?

Provider: Given your symptoms and physical exam findings, it could be a bacterial infection like strep throat or possibly a viral illness like the flu. I’d like to do a rapid strep test and possibly a flu test to confirm.

Patient: Okay. What do those tests involve?

Provider: The strep test involves swabbing the back of your throat, and the flu test is a nasal swab. Both are quick and should give us results within a few minutes.

Patient: That sounds fine. Let’s do it.

Provider: While we wait for the results, I want to discuss how you’ve been managing your symptoms. You mentioned ibuprofen hasn’t helped much. Have you tried anything else?

Patient: Just lozenges for my throat and warm tea, but they only help a little.

Provider: It’s good that you’re trying to stay hydrated. Have you had any ear pain or sinus pressure?

Patient: No ear pain, but some pressure around my forehead and eyes.

Provider: Have you had any recent travel?

Patient: No, I haven’t traveled anywhere recently.

Provider: Your rapid strep test came back positive, which means you likely have a bacterial infection.

Patient: Oh, that makes sense. So what’s the next step?

Provider: I’m going to prescribe you a 10-day course of antibiotics. It’s important to finish the full course even if you start feeling better in a few days.

Patient: Okay. Will the fever go down with the antibiotics?

Provider: Yes, the antibiotics should start working within 24 to 48 hours. You should start feeling better soon, but continue with fever management using ibuprofen or acetaminophen if needed. Also, get plenty of rest and drink fluids.

Patient: Got it. Is there anything else I should do?

Provider: Gargling with warm salt water can help soothe your throat. Avoid irritants like smoking or strong smells, and try to rest as much as possible. If your symptoms worsen or you develop trouble breathing, chest pain, or a rash, come back immediately.

Patient: That makes sense. Thanks for your help, doctor.

Provider: No problem! I’ll schedule a follow-up in a week to see how you’re doing.
"""

soap_note = """
Subjective:

-Patient reports a 7-day history of persistent cough, fever, sore throat, and fatigue.

-Symptoms include chills, night sweats, body aches, nasal congestion, mild headaches, and nausea.

-Fever has been unresponsive to ibuprofen.

-Swallowing is painful, reducing appetite.

-Reports exposure to a sick coworker one week ago.

Objective:

-Temperature: 102°F.

-Oxygen saturation: 97%.

-Throat examination: Redness with white patches on tonsils.

-Lungs: Clear upon auscultation.

-Nasal congestion noted.

-Rapid strep test: Positive.

Assessment:

-Acute bacterial pharyngitis (Strep Throat).

Plan:

-Prescribe 10-day course of antibiotics.

-Recommend continued hydration and rest.

-Symptom management with ibuprofen or acetaminophen.

-Gargle with warm salt water for sore throat relief.

-Follow-up in 7 days.

-Advise to return immediately if symptoms worsen or if breathing difficulties, chest pain, or rash develop.


"""