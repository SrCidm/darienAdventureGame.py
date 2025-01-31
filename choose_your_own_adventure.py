import time

# Selección de idioma
language = input("Choose your language / Elige tu idioma (English/Español): ").strip().lower()

if language == "english":
    messages = {
        "welcome": "🌎 Welcome to 'Crossing the Darién', an interactive adventure. 🌿🌊",
        "name": "What is your name? ",
        "start": "You are in the Darién jungle. The path splits: left or right. Which way do you choose? (left/right): ",
        "river": "After walking for hours, you reach a river. Do you swim across or look for a bridge? (swim/bridge): ",
        "swim_fail": "You tried to swim, but the current was too strong. ❌ Game over.",
        "bridge": "You found a bridge and crossed safely. ✅",
        "group": "You find a group of migrants. Do you join them or continue alone? (join/alone): ",
        "join_success": "The group helps you and you all reach Panama safely! 🎉",
        "alone_fail": "You get lost in the jungle and run out of supplies. ❌ Game over.",
        "coyote": "You meet a smuggler who offers to take you faster, but asks for money upfront. Do you pay or continue alone? (pay/alone): ",
        "pay_fail": "The smuggler steals your money and leaves you stranded. ❌ Game over.",
        "camp": "You find a migrant camp. Do you rest or keep walking? (rest/walk): ",
        "rest_success": "You recover and find help. ✅",
        "walk_fail": "You collapse from exhaustion in the jungle. ❌ Game over.",
        "final_choice": "You reach the Mexican border. Do you cross the desert or try to get a ride? (desert/ride): ",
        "desert_fail": "The desert is too harsh. ❌ Game over.",
        "ride_success": "You get a ride and finally reach the U.S.! 🇺🇸 Congratulations! Time to work hard! 💪",
        "invalid": "Invalid option. ❌ Game over.",
        "thanks": "Thanks for playing. Keep trying until you make it! 🚀"
    }
else:
    messages = {
        "welcome": "🌎 Bienvenido a 'Cruzando el Darién', una aventura interactiva. 🌿🌊",
        "name": "¿Cuál es tu nombre? ",
        "start": "Te encuentras en la selva del Darién. El camino se divide en dos: izquierda o derecha. ¿Cuál eliges? (izquierda/derecha): ",
        "river": "Después de caminar por horas, llegas a un río. ¿Cruzas nadando o buscas un puente? (nadar/puente): ",
        "swim_fail": "Intentaste nadar, pero la corriente era demasiado fuerte. ❌ Fin del juego.",
        "bridge": "Encontraste un puente y cruzaste con éxito. ✅",
        "group": "Te encuentras con un grupo de migrantes. ¿Te unes a ellos o sigues solo? (unirme/solo): ",
        "join_success": "El grupo te ayuda y juntos llegan a Panamá. 🎉",
        "alone_fail": "Te pierdes en la selva y te quedas sin provisiones. ❌ Fin del juego.",
        "coyote": "Te encuentras con un coyote que promete llevarte más rápido, pero pide dinero por adelantado. ¿Le pagas o sigues solo? (pagar/solo): ",
        "pay_fail": "El coyote te estafa y desaparece con tu dinero. ❌ Fin del juego.",
        "camp": "Llegas a un campamento de migrantes. ¿Descansas o sigues caminando? (descansar/seguir): ",
        "rest_success": "Te recuperas y encuentras ayuda. ✅",
        "walk_fail": "Sigues caminando sin descanso y colapsas por agotamiento. ❌ Fin del juego.",
        "final_choice": "Llegas a la frontera con México. ¿Cruzas por el desierto o intentas conseguir un aventón? (desierto/aventón): ",
        "desert_fail": "El desierto es demasiado duro. ❌ Fin del juego.",
        "ride_success": "¡Logras un aventón y finalmente llegas a EE.UU.! 🇺🇸 ¡Felicidades! Ahora a chambear. 💪",
        "invalid": "Opción no válida. ❌ Fin del juego.",
        "thanks": "Gracias por jugar. ¡Sigue intentando hasta lograrlo! 🚀"
    }

print(messages["welcome"])
name = input(messages["name"])
print(f"Hola, {name}. ¡Tu aventura comienza ahora!")

answer = input(messages["start"]).lower()

if answer == "izquierda" or answer == "left":
    answer = input(messages["river"]).lower()
    
    if answer == "nadar" or answer == "swim":
        print(messages["swim_fail"])
    elif answer == "puente" or answer == "bridge":
        print(messages["bridge"])
        answer = input(messages["group"]).lower()
        
        if answer == "unirme" or answer == "join":
            print(messages["join_success"])
            answer = input(messages["final_choice"]).lower()
            
            if answer == "desierto" or answer == "desert":
                print(messages["desert_fail"])
            elif answer == "aventón" or answer == "ride":
                print(messages["ride_success"])
            else:
                print(messages["invalid"])
        elif answer == "solo" or answer == "alone":
            print(messages["alone_fail"])
        else:
            print(messages["invalid"])
    else:
        print(messages["invalid"])

elif answer == "derecha" or answer == "right":
    answer = input(messages["coyote"]).lower()
    
    if answer == "pagar" or answer == "pay":
        print(messages["pay_fail"])
    elif answer == "solo" or answer == "alone":
        answer = input(messages["camp"]).lower()
        
        if answer == "descansar" or answer == "rest":
            print(messages["rest_success"])
            answer = input(messages["final_choice"]).lower()
            
            if answer == "desierto" or answer == "desert":
                print(messages["desert_fail"])
            elif answer == "aventón" or answer == "ride" or answer == "aventon":
                print(messages["ride_success"])
                quit()
            else:
                print(messages["invalid"])
        elif answer == "seguir" or answer == "walk":
            print(messages["walk_fail"])
        else:
            print(messages["invalid"])
    else:
        print(messages["invalid"])
else:
    print(messages["invalid"])

print(messages["thanks"])
