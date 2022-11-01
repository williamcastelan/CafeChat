# The script of the game goes in this file.
 
# Declare characters used by this game. The color argument colorizes the
# name of the character.


define c = Character("Cori", who_color="#2EC4B6")
define i = Character("You", who_color="#C39EFF")
define m = Character("Business Man", who_color="FC4B4B")
define p = Character("Princess", who_color="FC4B4B")
define k = Character("Karen")
define h = Character("Karen's Husband")
define o = Character("Pootie", who_color="#F5B7B1")
 
init:
    image cori normal = Image("cori normal.png")
    image cori angry = Image("cori angry.png")
    image cori question = Image("cori question.png")
    image bg room = Image("bg room.jpg")
    image man normal = Image("man normal.png")
    image man phone = Image("man phone.png")
    image man mad = Image("man mad.png")
    image man fear = Image("man fear.png")
    image princess = Image("princess.png")
    image karen normal = Image("karen normal.png")
    image karen mad = Image("karen mad.png")
    image karen husband = Image("karen husband.png")
    image pootie normal = Image("pootie normal.png")
    image pootie confused = Image("pootie confused.png")
    image pootie idea = Image("pootie idea.png")
    image pootie cafe = Image("pootie cafe.png")
    image sad dog = Image("sad dog.png")
   
    $ tip = int(0)
    $ badChoices = 0
    $ goodPootEnd = False
    $ stepsCorrect = 7
 
    default coriEnding = False
    default manEnding = False

 
 
# The game starts here.
 
label start:
    scene bg room

    play music "audio/fireflies.mp3"

    "You open the doors, already set up for another day of working at the Cafe."

    show cori normal
    with dissolve
  
    "A young college student enters the cafe, although a bit visibly stressed."
 
    i "Hello, welcome to the Cafe. What can I get started for you today?"
    c "Get me an iced mocha chocolate double espresso with whole milk. And make it fast would you?"
    i "What is the rush for?"
 
    show cori angry
 
    c "Damn Professor thinks he is untouchable with his tenure and treats anyone who is late like trash."
 
    menu:
        "Wow, I bet that sucks.":
            show cori normal
            $ tip = tip + 5
            i "Wow, I bet that sucks."
 
        "It can’t be THAT bad right?":
            i "It can’t be THAT bad right?"
 
 
    c "You wouldn’t believe what he does."
    c "He stops the whole class to berate the latecomer and when you get into the class and sit down he calls on you constantly and is so condescending."
    c "Not only that but he's so bad at teaching and never explains concepts."
    i "That sounds really annoying."
 
    show cori normal
 
    c "Yeah and everyone in class hates his guts. He is tenured though, and that makes people’s complaints useless."
    c "Now I’m stuck in this class that I need to pass for my finance degree."
    i "Is there really no way to get him out? Oh yeah, here’s your coffee."
    c "I don’t know. I complain and stuff but I feel like I should just grit my teeth and pass this class."
    i "Actually I’ve heard some students at Yule College created a petition and actually pressured the college to make a Professor undergo a tenure examination."
    i "Maybe you could give that a try?"
    c "Hmm. I don’t really know about that. Sounds like a huge hassle when I’ve only got a few months of this class left."
    c "Well, thanks for the coffee though."
 
    menu:
        "I get that, it is a lot of work":
            $ tip = tip + 5
            jump goodCoriEnding
        "You can’t complain if you don’t do anything about it.":
            jump badCoriEnding
 
 
    label goodCoriEnding:
        i "I get that, it is a lot of work. Just give it a thought though! Students don’t deserve to have to deal with teachers like that for a required class."
        c "Yeah… you make a point."
        c "Everyone that came before me in his class didn’t do anything about it and I guess the students after me also just have to suffer through his class…"
        i "No pressure! But change has to begin somewhere."
        c "Y'know what? Maybe I'll take up that idea on that petition thing."
        c "I've got a few friends in the school newspaper and I'm sure everyone in my class would sign if it is official enough. Thanks for listening to me rant."
        i "Its nothing! I wish you luck with the petition."
        c "Thank you. I'll come back to tell you how it goes!"
 
        hide cori
        with fade
 
        $ coriEnding = True
 
        "Cori has left the Cafe."
        "Your tip jar has [tip] dollars."
        jump businessManEnters
 
    label badCoriEnding:
        i "You can’t complain if you don’t do anything about it. Students that come after you are going to suffer too if you just let the professor do what he wants."
        show cori question
        c "Whats that got to do with me? With your logic the people before me should have done something. I just want to get my degree and go."
        i "Its just annoying when people complain when they can do something about it. Its like you have no backbone."
        c "What? Are you joking right now? I'm ranting about something and you're preaching at me?"
        c "What is wrong with you? Get off your high horse you work at a coffee shop."
        i "I'm only telling you my opinion, don't have to get all sensitive about it."
        c "SENSITIVE?!"
        show cori angry
        c "*splash* Keep your trashy coffee and opinions to yourself, no one asked."
        hide cori
        with fade
        "Cori has left the Cafe in a heap of rage."
        "You have coffee on your face and shirt as well as all over the countertops."
        "Your tip jar has [tip] dollars."
        jump businessManEnters
 
    label businessManEnters:
        show man phone
        with dissolve
        "You notice a man entering the Cafe gripping a leash in one hand and struggling to find a way to hold up a smartphone to his ear."
 
    i "Welcome to our Cafe. What can I get started for you today?"
 
    "The man slightly lowers his phone so he can hear your greeting while still engaged in a conversation."
 
    m "Make sure to keep the files separate. We don’t need any calls from HQ.."
    m "You did what?!"
    m "Okay, okay. This *really* isn’t a good time. I’m going to have to give you a callback so we can deal with this later."
    m "*hangs up*"
 
    show man normal
 
    m "Good afternoon! I have something to take care of so we need to make this quick."
    i "Yes, of course. You can order whenever you’re ready."
 
    if coriEnding == False:
        i "Also, please watch your step."
        i "There’s a puddle on the floor from a few minutes ago. I haven’t gotten a chance to mop it up yet."
        m "Uh, okay.."
        show man mad
        m "I’ve never heard of this place being so unsanitary."
        m "Can you just take my order so I can get out of here?"
   
    m "I need a venti Nitro Cold Brew to go and…"
    show man normal
    m "I’m wondering if you guys have anything that my little girl can drink."
    i "Little girl..?"
    show man normal at right
    show princess at left
    "The businessman picks up a feeble dog from the ground that you did not notice when the customer entered."
    "Your attention is brought to the chihuahua that seems like it’s one cough away from falling into its deathbed."
    m "Yes, this is my baby girl, Princess. She said she was in the mood for coffee today."
    m "Isn’t that right Princess?"
 
    "Not surprisingly, the dog failed to respond. The dog stays in the same position, not moving a muscle."
    "You examine the dog and watch drool dribble from it’s opened mouth. You hear a quiet groan as the dog’s protruding eyes lock onto you,"
    "forcing you to dart your gaze back to the businessman as if the dog can read your thoughts."
 
    menu:
        "Aw, she’s… adorable!":
            i "Aw, she’s… adorable!"
            $ tip = tip + 5
            jump adorable
        "Is it okay?":
            i "Is it okay?"
            jump isitokay
    hide princess
    show man normal at center
    label adorable:
        m "Thank you! I usually take her everywhere with me but the poor thing wasn’t feeling well today."
        m "so I decided to treat her to some coffee with me for her doing so well out of the house. Anything for her."
        $ tip = tip + 5
        jump mochabusiness
 
    label isitokay:
        m "She’s very happy to be here right now! I can tell!"
        m "I usually take her everywhere with me but the poor thing wasn’t feeling well today so I decided to treat her to some coffee with me for her doing so well out of the house."
 
    label mochabusiness:
        show man mad
        m "Just don’t give her any of that mocha business, she’s allergic to that."
 
    i "We do offer Puppachinos that are pet-friendly. No mocha. I’m sure your dog would love it!"
    show man normal
    m "Sounds good, then she’ll take one of those, please. And don’t forget my-"
    "The customer’s ringtone begins to blast from his hand interrupting his sentence."
    "The businessman briefly looks at his phone and takes a deep sigh."
    show man phone
    m "Excuse me. I have to take this outside"
    m "Can you please do me a favor and watch Princess for me? I’ll come back quickly."
    i "Sure. You can just leave her leash right there. *points to nearby chair*"
    "The businessman proceeds to follow your instructions and slightly gestures a wave to thank you before picking up the phone and finally cutting off the blaring ringtone."
    m "Yello? Yes, this is him."
    hide man
    with fade
    "His voice fades away as the man proceeds to open the door and exit the cafe. The cafe fills with the silence you’re used to except for the alarming dog left in your care."
    show princess at center
    "You try to think of what to do now after being left in this awkward situation."
 
    menu:
        "Attempt to diffuse":
            i "And then there were two…"
        "Tell a joke":
            i "Want to hear a joke?"
        "Staring Contest":
            i "Okay staring contest, 3.. 2.. 1.. Go!"
 
    p "…"
    "You shudder at the blank stare of the dog and decide to begin to make the businessman’s order."
    "You turn your back on the dog as you were busy preparing the venti coffee and Puppachino."
    "The cafe wasn’t particularly busy enough at the moment to be worried for the dog."
 
    if coriEnding:
        jump goodManEnding
    else:
        jump badManEnding
 
 
    label goodManEnding:
        i "Here you go, one venti Nitro Cold Brew and one Puppachino. *places the order on the countertop*"
        "The customer returns back to the Cafe in search of his pet to find her in the same place that he left her with a look of relief on his face."
        show man normal
        m "Thank you so much for watching her."
        "He pays for his order in haste and grabs his drinks. He extends his arm with the Puppachino towards Princess to give her a taste of the whipped cream-filled cup."
        m "I think she really likes it! Thank you again for watching Princess. I really appreciate it."
        i "No problem, sir. Have a great day."
        "The businessman exits the cafe."
        i "Another happy customer. I cannot wait to close up and get out of here!"
 
        hide man
        hide princess
        with fade
 
        $ manEnding = True
        $ tip = tip + 5
 
        "Business Man and Princess has left the Cafe."
        "Your tip jar has [tip] dollars."
        jump karenEnters
 
    label badManEnding:
        "The dog looks towards the puddle left by the previous customer and slowly drags itself toward it in a moment of curiosity."
        "After inspecting the puddle, the dog drinks from it as if it were a familiar puddle of water from its house."
        "Immediately after the dog lets out a cough that sounds like it’s been held back for a while and starts to wheeze."
        "As you hear this sound, you turn around in a panic and try to figure out what was wrong with the dog."
        "The wheeze gets progressively worse as time passes, and the dog eventually falls to the ground."
        show princess at left
        show man normal at right
        "The customer returns back to the Cafe with a look of relief on his face that quickly shifted to a face full of fear."
        m "Thank you for watching Princess for me-"
        show man fear
        m "OH MY GOD PRINCESS!! WHAT HAPPENED"
        "The man falls to his knees in front of the fainted dog."
        i "I didn’t do anything!! I swear! I just turned around and it looked like that."
        m "Oh really?? I could have this disgusting place shut down by tomorrow. I’ll let everyone know that you guys are after PEOPLE’S DOGS in here!"
        i "I-"
        i "I had my back turned and I swear I never touched \"Princess\".."
        m "Sure. And I’m going to call up every local critic and bring down your business’s reputation to make sure no one ever steps foot in here again."
        show man mad
        m "You just lost a valuable customer. And make sure to clean up next time. This place is filthy!!"
        hide man
        hide princess
        with fade
        "Business Man has left the Cafe in distress carrying his dog in his arms before you can get another word in."
        "You have been traumatized from posioning Princess."
        "Your tip jar has [tip] dollars."
        jump karenEnters
        
    label karenEnters:
        show karen normal
        with dissolve
        "A woman enters the Cafe looking peeved."
 
        i "Welcome! What can I get for you?"
        k "Yeah Hi. I would like- how old are you? Do your parents know you're here? Shouldn't you be in school?"
        i "Excuse me?"
        k "You look too young to work here."
        i "Ma'am I can assure you I am old enough to work here."
        show karen mad
        k "Don't you catch an attitude now! I was only looking out for you."
        i "Respectfully ma'am I am of age to work."
        show karen normal
        "Karen huffs"
        k "Get me a Medium Caramel Latte, with 5 pumps of Caramel, two shots of espresso, three cream, 4 sugar cane syrup, 10 pieces of ice and lots of whip cream with a drizzle of caramel."
        k "I can only have my latte a certain way and I WIll KNOW if you made it wrong."
        i "Right away ma'am."
        "Karen narrows her eyes, scrutinizing you."
        "You proceed to make the latte."
        k "You remember my order right? *she points her finger in accusation*"
        i "You asked for:"
 
        menu:
            "Medium Caramel latte":
                i "A Medium Caramel latte," 
            "Medium Vanilla Coffee":
                i "A Medium Vanilla Coffee,"
                show karen mad
                $ stepsCorrect = stepsCorrect - 1

        menu:
            i "with"
            "One shot of espresso":
                i "One shot of espresso"
                show karen mad
                $ stepsCorrect = stepsCorrect - 1
            "Two shots of espresso":
                i "Two shots of espresso"
                show karen normal

        menu:
            i "with like,"
            "No cream":
                i "No cream"
                show karen mad
                $ stepsCorrect = stepsCorrect - 1
            "Three cream":
                i "Three cream"
                show karen normal

        menu:
            i "and,"
            "4 sugar cane syrup":
                i "4 sugar cane syrup"
                show karen normal
            "4 splenda":
                i "4 splenda"
                show karen mad
                $ stepsCorrect = stepsCorrect - 1

        menu:
            i "along with,"
            "No ice":
                i "No ice"
                show karen mad
                $ stepsCorrect = stepsCorrect - 1
            "10 pieces of ice":
                i "10 pieces of ice"
                show karen normal

        menu:
            i "and"
            "No whipcream":
                i "No whipcream"
                show karen mad
                $ stepsCorrect = stepsCorrect - 1
            "Lots of Whipcream":
                i "Lots of Whipcream"
                show karen normal

        menu:
            i "And lastly"
            "Caramel drizzle":
                i "Caramel drizzle"
                show karen normal
            "Chocolate drizzle":
                i "Chocolate drizzle"
                show karen mad
                $ stepsCorrect = stepsCorrect - 1

        if stepsCorrect == 7:
            show karen normal
            i "Here you go ma'am."
            k "Hmph."
            i "Have a nice day- oh she's gone"
            $ tip = tip + 15
            hide karen
            with fade
            "Karen has left the Cafe, leaving a generous tip."
            "Your tip jar has [tip] dollars."
        elif stepsCorrect == 0:
            show karen mad
            k "I CAN'T BELIEVE THIS! HOW INCOMPETENT CAN YOU BE. Not only did you dare catch an attitude but you can't even make a proper latte!"
            i "Ma'am please calm down. It was a simple mist-"
            k "How dare you! That's it, I'm calling my husband!"
            show karen husband at left
            show karen mad at right
            with fade
            h "What's the problem honey?"
            k "Their coffee is HORRIBLE and so is their service!"
            h "Let's leave, I'm going to tell everyone how bad of a place this is. This won't be the last time you hear from us."
            hide karen
            hide karen husband
            with fade
            "Karen and her husband has left the Cafe in a rage, knocking your favorited potted plant onto the floor."
            "You lament as you realize you have to clean up something extra while closing the cafe today"
            "Your tip jar has [tip] dollars."
        else:
            show karen mad
            k "No no no, you are doing it wrong!! You stupid stupid worker! I want my money back! I knew it you incompetent #@#$#@."
            k "Wait until I tell everyone, as a matter of fact, I will be leaving a one star review."
            hide karen
            with fade
            "Karen has left the Cafe in a rage letting the door slam and the sound grates on your ears."
            "Your tip jar has [tip] dollars."
       

    label pootieEnters:
        show pootie normal
        with dissolve
    i "Welcome to the Cafe, what can I do for you?"
    o "Woah this is so cool, do you sell coffee?"
 
    menu:
        "Yep, what would you like?":
            i "Yep, what would you like?"
            o "Sweet, I want something strong and a lot of it."
        "Nope, but we have expired milk just for you :)":
            i "Nope but we have expired milk just for you :)"
            p "10/10, good service."
            $ badChoices = badChoices + 1
    
    "You serve them a drink"
    o "So, care to hear me out?"
 
    menu:
        "Of course, anything for my customers!":
            i "Of course, anything for my customers!"
        "Nah, don't wanna. I really need to get rid of that expired milk though.":
            i "Nah, don't wanna. I really need to get rid of that expired milk though."
            $ badChoices = badChoices +1
   
    show pootie idea
    o "Well then, if you were on a getaway, what would you use to escape?"
    show pootie normal
 
    menu:
        "Calm down there buddy.":
            i "Calm down there buddy."
            o "Aw c'mon, you're no fun."
        "A miniature dwarf elephant":
            i "A miniature dwarf elephant."
            o "That's a great idea, but wouldn't it be easy to get caught."
            $ badChoices = badChoices + 1
            menu:
                "Hm, maybe not actually.":
                    i "Hm, maybe not actually."
                    $ badChoices = badChoices - 1
                "Weaponize it, give it torpedoes that shoot out piranhas, the most violent ones possible!":
                    i "Weaponize it, give it torpedoes that shoot out piranhas, the most violent ones possible!"
                    $ badChoices = badChoices + 1
 
    show pootie idea
    o "Ooooo oooo, if you had the opportunity to steal anything in the world, what would it be?"
    show pootie normal
 
    menu:
        "Your heart, but seriously, stealing is a big no no.":
            i "Your heart, but seriously, stealing is a big no no."
            o "Fine fine, party pooper."
        "A lifetime supply of kindle eggs.":
            i "A lifetime supply of kindle eggs."
            o "That's a great idea, you're so smart, thanks for the drink :)"
            $ badChoices = badChoices + 1
        "Donald Trump's wig":
            i "Donald Trump's wig!"
            o "That's a great idea, you're so smart, thanks for the drink :)"
            $ badChoices = badChoices + 1
        "The World's Most Aggressive Baboon.":
            i "The World's Most Aggressive Baboon."
            o "That's a great idea, you're so smart, thanks for the drink :)"
            $ badChoices = badChoices + 1

    if badChoices > 3:
        jump badPootEnd
    else:
        jump neutralPootEnd
   
    label badPootEnd:
        show sad dog
        "You were arrested as an accomplice for murder after a bystander dog was buried under a pile of piranhas after Pootie's getaway :("
        "R.I.P"
        return
   
    label neutralPootEnd:
        o "It really is great getting to do what you want. You get me, right?"
        i "Hm, yeah. I think I understand."
        o "Even if it's silly, what matters to me is that its fun!"
        i "True, but look after yourself too. Its nice that you're enjoying yourself, but isn't it sad if you can no longer have fun."
        show pootie confused
        o "I don't really know. I'm so confused."
        show pootie normal
        i "I admire your energy though, but the things you do don't have to be so...um reckless. You can have fun with things that are calm too!"
        show pootie confused
        o "Woah, something calm can also be fun? Oooo, like what kind of stuff?"
        show pootie normal
        i "Hm let's say running a coffee shop, it's great meeting new people and seeing my regulars. But that's just me."
        o "Talking to me would be really fun, right?"
        i "True true, but why not give it a shot with less risky things?"
        o "Just a thought, but you wouldn't happen to be hiring?"
       
        menu:
            "I'll admit, it would be nice to have someone helping around.":
                i "I'll admit, it would be nice to have someone helping around."
                $ goodPootEnd = True
            "Nope, hard pass with your help.":
                i "Nope, hard pass with your help."
                $ badPootEnd2 = badPootEnd + 1

        if goodPootEnd == True:
            "One week later"
            show pootie cafe
            "Pootie turned a new leaf and is now a new employee at the Cafe"
            ":)"
        else:
            show sad dog
            "Pootie is arrested for murder after a bystander dog was buried by piranhas during her robbery getaway"
            "R.I.P :("
            
        
 
    return