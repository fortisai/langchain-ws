from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model_name="claude-3-5-sonnet-20241022")
llm.invoke("Hello, world!")
