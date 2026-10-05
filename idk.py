import time;

while True:
    print("--- MENU ---")
    print("1. Celsius para Fahrenheit")
    print("2. Celcius para Kelvin")
    print("3. Fahrenheit para Celcius")
    print("4. Fahrenheit para Kelvin")
    print("5. Kelvin para Celcius")
    print("6. Kelvin para Fahrenheit")
    print("0. Sair ")

    opcao = input ("Que converção deseja fazer (0-6): ")
    
    if opcao == "1":
        entrada = input("Digite o valor em Celcius: ")
        
        celcius = float(entrada)

        Fahrenheit = (celcius * 1.8) + 32
        print(f"{celcius} Celcius equivalem a {Fahrenheit} Fahrenheits.")
        time.sleep(2.5) 

    elif opcao == "2":
            entrada = input("Digite o valor em Celcius: ")
            
            celcius = float(entrada)
    
            kelvin = celcius + 273.15
            print(f"{celcius} Celcius equivalem a {kelvin} Kelvins.")
            time.sleep(2.5)

    elif opcao == "3":
                entrada = input("Digite o valor em Fahrenheit: ")
                
                Fahrenheit = float(entrada)
        
                celcius = (Fahrenheit - 32) *  5/9
                print(f"{Fahrenheit} Fahrenheit equivalem a {celcius} Celcius.")
                time.sleep(2.5)

    elif opcao == "4":
                entrada = input("Digite o valor em Fahrenheit: ")
                
                Fahrenheit = float(entrada)
        
                kelvin = (Fahrenheit - 32) *  5/9 + 273.15
                print(f"{Fahrenheit} Fahrenheit equivalem a {kelvin} Kelvins.")
                time.sleep(2.5)

    elif opcao == "5":
                    entrada = input("Digite o valor em Kelvin: ")
                    
                    kelvin = float(entrada)
            
                    celcius = kelvin -273.15
                    print(f"{kelvin} Kelvin equivalem a {celcius} Celcius.")
                    time.sleep(2.5)

    elif opcao == "6":
                    entrada = input("Digite o valor em Kelvin: ")
                    
                    kelvin = float(entrada)
            
                    Fahrenheit = 1.8 * (kelvin - 273.15) + 32
                    print(f"{kelvin} Kelvin equivalem a {Fahrenheit} Fahrenheits.")
                    time.sleep(2.5)

    elif opcao == "0":
                   print("Saindo do sistema. Até logo!")
                   break
    else:
        print("Opção inválida! Tente novamente.")                

       
    