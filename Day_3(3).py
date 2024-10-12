print('''
*******************************************************************************
              /-_-"'
            /_||||||``
           /_'. _|\||`
        \ / '-. _ |\|
        < ``-.;),--'`
        '--. |__--__-`
     /-/-/|o|-|\-|\ |\ | 
       '`  ` |-|   `` '               |") |_" (_" /"' | | |_" |"\|/
             |-|                      |"\ |__ ,_) \_, |_| |__ |_/  o  o  o
             |-|O
             |-(\,__
          ...|-|\--,\_....
      ,;;;;;;;;;;;;;;;;;;;;;;;;,.
~~,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go?")
road = input('\tType "left" or "right"').lower()
if road == "left":
    print('''
 _       _        
| |     | |       
| | __ _| | _____ 
| |/ _` | |/ / _ |
| | (_| |   <  __/
|_|\__,_|_|\_\___|''')
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake = input('\tType "wait" to wait for a boat. Type "swim" to swim across. ').lower()

    if lake == "wait":
        print('''
            ______
   ,-' ;  ! `-.
  / :  !  :  . ]
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|
            ______
   ,-' ;  ! `-.
  / :  !  :  .  }
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|

     ______
   ,-' ;  ! `-.
  / :  !  :  . -
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|
 ''')
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        island = input('\tOne red, one yellow and one blue. Which colour do you choose? ').lower()
        if island == "yellow":
            print("You found the treasure! You Win!")
        elif island == "red":
            print("It's a room full of fire. Game Over.")
        else:
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")