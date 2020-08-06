class Data():
    bike_names = ["CLASSIC", "BULLET", "THUNDERBIRD", "INTERCEPTOR", "INTERCEPTOR", "HIMALAYAN"]
    bike_prices = ["1000", "2000", "3000", "4000", "5000", "6000"]
    bike_number = ['001', "002", "003", "004", "005", "006"]
    bike_weight = ["100kgs", "200kgs", "300kgs", "400kgs", "500kgs", "600kgs"]

class marketer(Data):
    def __init__(self):
        print("marketing...")
    def print_menu(self):
        for i in range(len(Data.bike_names)):
            print(i+1,Data.bike_names[i])
            
    def print_details(self,user_entered_name):
        print("{:<10} {:<10} {:<10} {:<10}".format("NAME","PRICE","NUMBER","WEIGHT"))
        for i in range(len(Data.bike_names)):

            if user_entered_name == Data.bike_names[i] :
                print("{:<10} {:<10} {:<10} {:<10}".format(Data.bike_names[i],Data.bike_prices[i],Data.bike_number[i],Data.bike_weight[i]))

class User():
    name = "ijaz"
    def __init__(self):
        pass
    def take_input(self):
        name_of_bike = input("please select the bike :")
        return name_of_bike



ob=marketer()
ob.print_menu()
name = User().take_input().upper()


while name != "STOP":
    ob.print_details(name)
    name = User().take_input().upper()

    name = User().name
    if name==name:
        print("this bike belongs to:",name)


print("")


