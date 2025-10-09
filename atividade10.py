import os
os.system("cls")

for i in range (1):
    peso = float(input("informe seu peso: "))
    altura = float(input("inform sua altura: "))

def imc(peso, altura):
    return (altura*2)+(peso/altura) 

reposta_imc = imc(peso, altura)

match reposta_imc:
    
    case 1:
        imc < 18.5
        print("Abaixo do peso\nConsulte um nutricionista para orientação")
    case 2:
        imc <= 18.5 or 24.9
        print("peso Noarmal\nMantenha hábitos saudáveis!")
    case 3:
        imc >= 25 or 29.9
        print("Sobrepeso\nconside uma dieta balanceada e atividade fisica")
    case 4:
        imc >= 30 or 34.9
        print("obesidade grau 1\nprocure orientação de um proficional de saúde")
    case 5:
        imc >= 35 or 39.9
        print("obesidade grau 2\n consulte um médico para avaliação e orientação")
    case 6:
        imc >= 40 or 100
        print("obesidade grau 3\n busque assistencia médica imediatamente")
    case _:
        print("")

print(f"{reposta_imc:.2f}")