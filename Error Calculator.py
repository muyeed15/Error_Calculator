print("--<< Error Calculator >>--\
      \n--------By Muyeed---------\
      \n\n< Calculate your experiment data errors! >\n")
def error_calculator():
    class Stack():
        def __init__(self):
            self.data_in = []
            self.data_ex = []
            self.data_er = []
        
        def push_in(self, data):
            self.data_in.append(data)
        
        def push_ex(self, data):
            self.data_ex.append(data)
        
        def push_er(self, data):
            self.data_er.append(data)
        
        def show_Stack(self):
            print(self.data_in)
            print(self.data_ex)
            print(self.data_er)
        
        def show_Error(self):
            avg = 0
            for k in range(0, len(self.data_er)):
                if k == 0:
                    print("\n--<< Error Calculation >>--\n")
                print(f"C{k+1}: {self.data_in[k]}, E{k+1}: {self.data_ex[k]} >> Error: {self.data_er[k]} %")
                avg += float(self.data_er[k])
            
            avg = "%.4f" % float(avg/len(self.data_er))
            print(f"Average Error: {avg} %")
            
            def ask_q():
                print("\n")
                ask = (input("Do you want to start over again? (Y/N): ")).upper()
                if ask == "Y":
                    print("\n")
                    error_calculator()
                elif ask == "N":
                    exit
                else:
                    print("Invalid Input!")
                    ask_q()
            
            ask_q()

    main = Stack()

    def data_input():
        dat_num = int(input("Number of data to input: "))
        print("--<< Enter your data >>--\
            \n\nC = Collected Data, E = Expected Data")
        
        for i in range(1, dat_num+1):
            print(f"\nData {i}:")
            in_dat = float(input(f"C{i}>> "))
            main.push_in(in_dat)

            ex_dat = float(input(f"E{i}>> "))
            main.push_ex(ex_dat)

            er_dat = ((in_dat-ex_dat)/in_dat)*100
            if er_dat < 0:
                er_dat = -(er_dat)
            else:
                er_dat = er_dat
            main.push_er("%.4f" % (er_dat))

    data_input()
    main.show_Error()

error_calculator()