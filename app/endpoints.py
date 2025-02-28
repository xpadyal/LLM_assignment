from langchain_core.runnables import RunnableLambda
from chain import custom_chain

# Wrap the custom chain function for the /ask endpoint
wrapped_chain = RunnableLambda(custom_chain)

