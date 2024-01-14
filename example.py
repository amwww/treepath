from main import *

main = Tree()

main.add_main(prompt='Hello and Welcome to your adventure! What would you like to do?', outcomes=['Take a bath', 'Go outside', 'Touch grass'])
main.main.add_outcome('Take a bath', 'result', main.main, 'You took a bath. Why would you wanna be cleaner?')
main.main.add_outcome('Touch grass', 'result', main.main, 'You touched grass. Your immune cells didn\'t know what it is and formed an alergic reaction.\nYou died.')
main.main.add_outcome('Go outside', 'What would you like to do now?', ['Go back inside', 'Stare at the sun', 'Cross the road', 'Stay outside', 'Talk to the neighbour', 'Sit and chill'], 'You went outside to enjoy some fresh air.')

main.main.outcomes['Go outside'].add_outcome('Go back inside', 'You walk inside your house. What\'s next?', ['Go back to your room', 'Lock the door', 'Go outside again'], 'You went back inside.')
main.main.outcomes['Go outside'].outcomes['Go back inside'].add_outcome('Go back to your room', 'result', main.main, 'You went back into your room.')
main.main.outcomes['Go outside'].outcomes['Go back inside'].add_outcome('Lock the door', 'result', main.main, 'You realise you didn\'t lock the door this whole time. You lock the door, and go back to your room.')
main.main.outcomes['Go outside'].outcomes['Go back inside'].add_outcome('Go outside again', 'result', main.main.outcomes['Go outside'], 'You go back outside.')

main.main.outcomes['Go outside'].add_outcome('Stare at the sun', 'result', main.main, 'You look at the sun considering your life choices. As the sun burns your eyes, you realise how worthless you are to make this desicion. You died.')

main.main.outcomes['Go outside'].add_outcome('Cross the road', 'result', main.main, 'Your neighbour watches you cross the road. He watches as he screams at you, "FOR THE SIX MILIIONTH NINE HUNDRED FOUR HUNDRED AND SENVENTY THIRD TIME, THERES NO OTHER SIDE OF THE ROAD. ITS A CLIFF, STEVE." You died of fall damage.')


while True: 
    main.step()
