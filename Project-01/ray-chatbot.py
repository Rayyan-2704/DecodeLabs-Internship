"""
    DecodeLabs Internship - Project 01
    Author: Rayyan Aamir
    Project Description: A simple rule-based chatbot that responds to predefined user inputs using control flow (if-else) logic
"""

class RuleBasedChatbot:
    def __init__(self):
        self.name = "RayBot"
        self.exit_commands = ["quit", "exit", "end", "stop", "bye", "goodbye"]
        self.knowledge_base = {
            "hello": f"Hello! I'm {self.name}, a rule-based chatbot. How can I help you today?",
            "hi": "Hi there! What's on your mind? Ask me anything or type 'help'",
            "name": f"My name is {self.name}, your friendly rule-based chatbot assistant",
            "joke": "Why do programmers prefer dark mode? Because light attracts bugs xD",
            "weather": "Sorry, I am not proficient enough to provide weather status :(",
            "help": "You can ask me about my name, to tell a joke, about the weather or just say hello :) !"
        }

    def get_response(self, user_input):
        for prompt, response in self.knowledge_base.items():
            if prompt in user_input:
                return response
            
        return "I'm not completely sure I understood that. Could you try paraphrasing? (Type 'help' for ideas)"
    
    def run(self):
        print(f"[{self.name}]: Online and ready! (Type 'exit' to end session)")
        print("-" * 70)

        while True:
            try:
                user_input = input("You: ").strip().lower()

                if not user_input:
                    continue

                for command in self.exit_commands:
                    if command in user_input:
                        print(f"[{self.name}]: Time to rest. Goodbye!")
                        return

                response = self.get_response(user_input)
                print(f"[{self.name}]: {response}")
                print("-" * 70)

            except (KeyboardInterrupt, EOFError):
                print(f"\n[{self.name}]: Emergency shutdown triggered. Goodbye!")
                break


if __name__ == "__main__":
    chatbot = RuleBasedChatbot()
    chatbot.run()