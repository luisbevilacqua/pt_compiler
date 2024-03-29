class StoreProgram():
    def __init__(self, language, output_file):
        self.target_content = ""
        self.language = language
        self.output_file = output_file
        self.declared_variables = dict()
        print(
            f"Hello, Companheiro! "
            f"You're compiling from PT to {self.language}."
        )
    
    def already_declared(self, identifier):
        return identifier in self.declared_variables.keys()
    
    def types_match(self, variable, type_to_compare):
        return self.declared_variables[variable] == type_to_compare

    def get_type(self, variable):
        return self.declared_variables[variable]


    def add_variable(self, variable_type, identifier):
        # print(f"Storing {identifier} with type {variable_type}")
        self.declared_variables[identifier] = variable_type

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
