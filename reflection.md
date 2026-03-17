# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
I think it was fairly straightforward. Especially what it wanted me to do and how to play. Everything was labeled pretty well 


- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - The hints of go lower and go higher are off. 
  - It lets you enter numbers below 1. 
  - The buttons are lowkey kinda glitchy especially new game, I don't think that one works. 

  Note: I will be focusing on the first two bugs to fix. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI fix for the go higher and go lower guidance was correct, I verified by letting the agent make the changes and then I ran it and if it worked kept it. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
It kept messing up the error message for out of range values so I had to be very specific in my prompt. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tested it. And I tried to fix a very specific bug at at ime. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  Entering numbers out of range, it showed me whether it was detecting the number is out of range. 
- Did AI help you design or understand any tests? How?
Yeah it helped me come up with edgecases very quickly which was very helpful and helped me ensure the functionality is tested well. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
It reminds me of react ui but way easier. Its basically like running ur website or something. Pretty cool. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I like how specific I was with my prompts and my strategy of splitting up core logic and ui logic first while keeping game logic, and then fixing bugs. 
- What is one thing you would do differently next time you work with AI on a coding task?
I wish I committed after every perfect fix so that I could roll back when copilot messed up which it did a lot. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I think how you prompt it and the order you go in and how you save the code and going piece by piece really matters. Sometimes things change so entirely like copilot completely messed up the ui. So like you have to be careful, have backup, and be able to roll back to use copilot effectively and efficiently. 
