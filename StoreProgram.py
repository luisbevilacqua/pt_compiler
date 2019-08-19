class StoreProgram():
    def __init__(self, language, output_file):
        self.target_content = ""
        self.language = language
        self.output_file = output_file
        print(
            f"Hello, Companheiro! "
            f"You're compiling from PT to {self.language}."
        )
    
    def ugly_pretty_print(self):
        self.target_content = self.target_content.replace('{','{\n').replace('}','}\n').replace(';',';\n')

    def append(self, code): 
        self.target_content += code
    
    def save_content(self):
        with open(self.output_file, 'w') as output_file:
            output_file.write(self.target_content)
        return

    def show_content(self):
        print(self.target_content)
        return

    def __del__(self):
        self.ugly_pretty_print()
        if self.output_file:
            self.save_content()
            print(
                f"Companheiro, your program was saved in {self.output_file}."
            )
        else:
            self.show_content()
        return
