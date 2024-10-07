GENERIC_PROMPT = '''Given the following text file, generate a list of questions and answers someone might ask about 
the city described in the document. It should also mention questions on how to reach the city from different 
locations and information about its history, things to do, things to see, accommodations, restaurants, food, 
and nightlife. Generate the result in the form of JSON in the following format: {"city": "...", "q_a": [{"q": "...", 
"a": "..."}, {"q": "...", "a": "..."}, ...]} '''

SUSTAINABILITY_PROMPT = '''Given the following text file, generate a list of questions and answers highlighting 
sustainable travel or related to sustainable tourism or sustainability in general. Someone might ask about the city 
described in the document. Generate the result in the form of JSON in the following format: {"city": "...", 
"q_a": [{"q": "...", "a": "..."}, {"q": "...", "a": "..."}, ...]} '''

LLAMA_PROMPT = '''You will be provided with a paragraph of text in the wiki format. Your task is to generate a 
structured set of questions and answers based on the information contained within the paragraph. The questions should 
cover key details, facts, and concepts mentioned in the text. Each question should be directly answerable using the 
information from the paragraph. Follow these steps: Read the provided paragraph carefully. Identify the main points, 
facts, and details in the paragraph. Use this information to generate a set of questions that cover the essential 
aspects of the text and require specific answers. Don't ask yes/no questions; aim for open-ended questions that delve 
into the content and don't only ask factual questions. Formulate clear and concise questions that a reader might ask 
to understand the paragraph better. Provide accurate answers to each of the questions based on the information in the 
paragraph. The answers should be complete and informative, addressing the core of the question. You can expand on the 
information provided in the paragraph to create comprehensive answers. Do not name the paragraph in the questions or 
answers. The questions should be complex and nuanced! I repeat, the questions should be complex and nuanced! I again 
repeat, the questions should be complex and nuanced! 
The structure of the questions and answers should be as follows: {"city": "...", "q_a": [{"q": "...", "a": "..."},
Paragraph:'''


