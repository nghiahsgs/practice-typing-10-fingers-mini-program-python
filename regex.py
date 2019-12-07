import re
regex1=re.compile(r'"(.*)"')
regex1=re.compile(r'\d. (.*)')
regex1=re.compile(r'([A-Z](.*?))\.')
regex1=re.compile(r'“(.*?)”')
ndung='''
1. Your limitation—it’s only your imagination.

2. Push yourself, because no one else is going to do it for you.

3. Sometimes later becomes never. Do it now.

4. Great things never come from comfort zones.

5. Dream it. Wish it. Do it.

6. Success doesn’t just find you. You have to go out and get it.

7. The harder you work for something, the greater you’ll feel when you achieve it.

8. Dream bigger. Do bigger.

9. Don’t stop when you’re tired. Stop when you’re done.

10. Wake up with determination. Go to bed with satisfaction.

11. Do something today that your future self will thank you for.

12. Little things make big days.

13. It’s going to be hard, but hard does not mean impossible.

14. Don’t wait for opportunity. Create it.

15. Sometimes we’re tested not to show our weaknesses, but to discover our strengths.

16. The key to success is to focus on goals, not obstacles.

17. Dream it. Believe it. Build it.
'''
ndung='''
1. "If you want to achieve greatness stop asking for permission." --Anonymous
2. "Things work out best for those who make the best of how things work out." --John Wooden
3. "To live a creative life, we must lose our fear of being wrong." --Anonymous
4. "If you are not willing to risk the usual you will have to settle for the ordinary." --Jim Rohn
5. "Trust because you are willing to accept the risk, not because it's safe or certain." --Anonymous
6. "Take up one idea. Make that one idea your life--think of it, dream of it, live on that idea. Let the brain, muscles, nerves, every part of your body, be full of that idea, and just leave every other idea alone. This is the way to success." --Swami Vivekananda
7. "All our dreams can come true if we have the courage to pursue them." --Walt Disney
8. "Good things come to people who wait, but better things come to those who go out and get them." --Anonymous
9. "If you do what you always did, you will get what you always got." --Anonymous
10. "Success is walking from failure to failure with no loss of enthusiasm." --Winston Churchill
11. "Just when the caterpillar thought the world was ending, he turned into a butterfly." --Proverb
12. "Successful entrepreneurs are givers and not takers of positive energy." --Anonymous
13. "Whenever you see a successful person you only see the public glories, never the private sacrifices to reach them." --Vaibhav Shah
14. "Opportunities don't happen, you create them." --Chris Grosser
15. "Try not to become a person of success, but rather try to become a person of value." --Albert Einstein
16. "Great minds discuss ideas; average minds discuss events; small minds discuss people." --Eleanor Roosevelt
17. "I have not failed. I've just found 10,000 ways that won't work." --Thomas A. Edison
18. "If you don't value your time, neither will others. Stop giving away your time and talents--start charging for it." --Kim Garst
19. "A successful man is one who can lay a firm foundation with the bricks others have thrown at him." --David Brinkley
20. "No one can make you feel inferior without your consent." --Eleanor Roosevelt
21. "The whole secret of a successful life is to find out what is one's destiny to do, and then do it." --Henry Ford
22. "If you're going through hell keep going." --Winston Churchill
23. "The ones who are crazy enough to think they can change the world, are the ones who do." --Anonymous
24. "Don't raise your voice, improve your argument." --Anonymous
25. "What seems to us as bitter trials are often blessings in disguise." --Oscar Wilde
26. "The meaning of life is to find your gift. The purpose of life is to give it away." --Anonymous
27. "The distance between insanity and genius is measured only by success." --Bruce Feirstein
28. "When you stop chasing the wrong things, you give the right things a chance to catch you." --Lolly Daskal
29. "I believe that the only courage anybody ever needs is the courage to follow your own dreams." --Oprah Winfrey
30. "No masterpiece was ever created by a lazy artist." --Anonymous
31. "Happiness is a butterfly, which when pursued, is always beyond your grasp, but which, if you will sit down quietly, may alight upon you." --Nathaniel Hawthorne
32. "If you can't explain it simply, you don't understand it well enough." --Albert Einstein
33. "Blessed are those who can give without remembering and take without forgetting." --Anonymous
34. "Do one thing every day that scares you." --Anonymous
35. "What's the point of being alive if you don't at least try to do something remarkable." --Anonymous
36. "Life is not about finding yourself. Life is about creating yourself." --Lolly Daskal
37. "Nothing in the world is more common than unsuccessful people with talent." --Anonymous
38. "Knowledge is being aware of what you can do. Wisdom is knowing when not to do it." --Anonymous
39. "Your problem isn't the problem. Your reaction is the problem." --Anonymous
40. "You can do anything, but not everything. --Anonymous
41. "Innovation distinguishes between a leader and a follower." --Steve Jobs
42. "There are two types of people who will tell you that you cannot make a difference in this world: those who are afraid to try and those who are afraid you will succeed." --Ray Goforth
43. "Thinking should become your capital asset, no matter whatever ups and downs you come across in your life." --A.P.J. Abdul Kalam
44. "I find that the harder I work, the more luck I seem to have." --Thomas Jefferson
45. "The starting point of all achievement is desire." --Napoleon Hill
46. "Success is the sum of small efforts, repeated day-in and day-out." --Robert Collier
47. "If you want to achieve excellence, you can get there today. As of this second, quit doing less-than-excellent work." --Thomas J. Watson
48. "All progress takes place outside the comfort zone." --Michael John Bobak
49. "You may only succeed if you desire succeeding; you may only fail if you do not mind failing." --Philippos
50. "Courage is resistance to fear, mastery of fear--not absence of fear." --Mark Twain
51. "Only put off until tomorrow what you are willing to die having left undone." --Pablo Picasso
52. "People often say that motivation doesn't last. Well, neither does bathing--that's why we recommend it daily." --Zig Ziglar
53. "We become what we think about most of the time, and that's the strangest secret." --Earl Nightingale
54. "The only place where success comes before work is in the dictionary." --Vidal Sassoon
55. "Too many of us are not living our dreams because we are living our fears. " --Les Brown
56. "I find that when you have a real interest in life and a curious life, that sleep is not the most important thing." --Martha Stewart
57. "It's not what you look at that matters, it's what you see." --Anonymous
58. "The road to success and the road to failure are almost exactly the same." --Colin R. Davis
59. "The function of leadership is to produce more leaders, not more followers." --Ralph Nader
60. "Success is liking yourself, liking what you do, and liking how you do it." --Maya Angelou
61. "As we look ahead into the next century, leaders will be those who empower others." --Bill Gates
62. "A real entrepreneur is somebody who has no safety net underneath them." --Henry Kravis
63. "The first step toward success is taken when you refuse to be a captive of the environment in which you first find yourself." --Mark Caine
64. "People who succeed have momentum. The more they succeed, the more they want to succeed, and the more they find a way to succeed. Similarly, when someone is failing, the tendency is to get on a downward spiral that can even become a self-fulfilling prophecy." --Tony Robbins
65. "When I dare to be powerful, to use my strength in the service of my vision, then it becomes less and less important whether I am afraid." --Audre Lorde
66. "Whenever you find yourself on the side of the majority, it is time to pause and reflect." --Mark Twain
67. "The successful warrior is the average man, with laser-like focus." --Bruce Lee
68. "There is no traffic jam along the extra mile." --Roger Staubach
69. "Develop success from failures. Discouragement and failure are two of the surest stepping stones to success." --Dale Carnegie
70. "If you don't design your own life plan, chances are you'll fall into someone else's plan. And guess what they have planned for you? Not much." --Jim Rohn
71. "If you genuinely want something, don't wait for it--teach yourself to be impatient." --Gurbaksh Chahal
72. "Don't let the fear of losing be greater than the excitement of winning." --Robert Kiyosaki
73. "If you want to make a permanent change, stop focusing on the size of your problems and start focusing on the size of you!" --T. Harv Eker
74. "You can't connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future. You have to trust in something--your gut, destiny, life, karma, whatever. This approach has never let me down, and it has made all the difference in my life." --Steve Jobs
75. "Two roads diverged in a wood and I  took the one less traveled by, and that made all the difference." --Robert Frost
76. "The number one reason people fail in life is because they listen to their friends, family, and neighbors." --Napoleon Hill
77. "The reason most people never reach their goals is that they don't define them, or ever seriously consider them as believable or achievable. Winners can tell you where they are going, what they plan to do along the way, and who will be sharing the adventure with them." --Denis Waitley
78. "In my experience, there is only one motivation, and that is desire. No reasons or principle contain it or stand against it." --Jane Smiley
79. "Success does not consist in never making mistakes but in never making the same one a second time." --George Bernard Shaw
80. "I don't want to get to the end of my life and find that I lived just the length of it. I want to have lived the width of it as well." --Diane Ackerman
81. "You must expect great things of yourself before you can do them." --Michael Jordan
82. "Motivation is what gets you started. Habit is what keeps you going." --Jim Ryun
83. "People rarely succeed unless they have fun in what they are doing." --Dale Carnegie
84. "There is no chance, no destiny, no fate, that can hinder or control the firm resolve of a determined soul." --Ella Wheeler Wilcox
85. "Our greatest fear should not be of failure but of succeeding at things in life that don't really matter." --Francis Chan
86. "You've got to get up every morning with determination if you're going to go to bed with satisfaction." --George Lorimer
87. "A goal is not always meant to be reached; it often serves simply as something to aim at." -- Bruce Lee
88. "Success is ... knowing your purpose in life, growing to reach your maximum potential, and sowing seeds that benefit others." --John C. Maxwell
89. "Be miserable. Or motivate yourself. Whatever has to be done, it's always your choice." --Wayne Dyer
90. "To accomplish great things, we must not only act, but also dream, not only plan, but also believe." --Anatole France
91. "Most of the important things in the world have been accomplished by people who have kept on trying when there seemed to be no help at all." --Dale Carnegie
92. "You measure the size of the accomplishment by the obstacles you had to overcome to reach your goals." --Booker T. Washington
93. "Real difficulties can be overcome; it is only the imaginary ones that are unconquerable." --Theodore N. Vail
94. "It is better to fail in originality than to succeed in imitation." --Herman Melville
95. "What would you do if you weren't afraid." --Spencer Johnson
96. "Little minds are tamed and subdued by misfortune; but great minds rise above it." --Washington Irving
97. "Failure is the condiment that gives success its flavor." --Truman Capote
98. "Don't let what you cannot do interfere with what you can do." --John R. Wooden
99. "You may have to fight a battle more than once to win it." --Margaret Thatcher
100. "A man can be as great as he wants to be. If you believe in yourself and have the courage, the determination, the dedication, the competitive drive and if you are willing to sacrifice the little things in life and pay the price for the things that are worthwhile, it can be done." --Vince Lombardi'''

ndung='''

Everything you’ve ever wanted is on the other side of fear. — George Addair

Pain is temporary. Quitting lasts forever. – Lance Armstrong

The pain you feel today will be the strength you feel tomorrow. – Unknown

We must embrace pain and burn it as fuel for our journey. – Kenji Miyazawa

A problem is a chance for you to do your best. – Duke Ellington

Hard times don’t create heroes. It is during the hard times when the ‘hero’ within us is revealed. – Bob Riley



Whatever is worrying you right now, forget about it. Take a deep breath, stay positive and know that things will get better. – Unknown

It’s not about perfect. It’s about effort. – Jillian Michaels

Believe you can and you’re halfway there. – Theodore Roosevelt

Challenges are what make life interesting. Overcoming them is what makes them meaningful.

You are so much more than what you are going through. – John Tew

Passion first and everything will fall into place. – Holly Holm






Difficult roads always lead to beautiful destinations. – Zig Ziglar

Staying positive does not mean that things will turn out okay. Rather it is knowing that you will be okay no matter how things turn out. – Unknown



Goals may give focus, but dreams give power. – John Maxwell

Don’t wish it were easier. Wish you were better. ― Jim Rohn

Your mind is a powerful thing. When you fill it with positive thoughts, your life will start to change.

Hustle until you no longer have to introduce yourself.

Success is what happens after you have survived all of your disappointments.

You don’t always get what you wish for. But you always get what you work for.

You don’t find will power, you create it.

Once you choose hope, anything’s possible. – Christopher Reeve

Push yourself because no one else is going to do it.

You cannot fail at being yourself. – Wayne Dyer

Don’t wait for opportunity. Create it.

You are the only one who can limit your greatness. – Unknown

The first and greatest victory is to conquer self. – Plato

Results happen over time, not overnight. Work hard, stay consistent, and be patient.

With confidence you have won before you have started. – Marcus Garvey

Success is what comes after you stop making excuses. – Luis Galarza

You don’t want to look back and know you could have done better.




The moment you doubt whether you can fly, you cease for ever to be able to do it. – J.M. Barrie

Be so good they can’t ignore you. – Steve Martin

You will never always be motivated. You have to learn to be disciplined.

Believe in yourself! Have faith in your abilities! Without a humble but reasonable confidence in your own powers you cannot be successful or happy. – Norman Vincent Peale

When you know what you want, and want it bad enough, you’ll find a way to get it. – Jim Rohn

The best way to gain self-confidence is to do what you are afraid to do. – Swati Sharma

Motivation is what gets you started. Habit is what keeps you going. – Jim Rohn

Never stop trying. Never stop believing. Never give up. Your day will come. – Unknown

Results happen over time, not overnight. Work hard, stay consistent, and be patient. – Unknown

Our greatest glory is not in never falling, but in rising every time we fall. — Confucius

Success is what happens after you have survived all of your disappointments. – Unknown

Don’t try to be perfect. Just try to be better than you were yesterday. – Unknown

Start where you are. Use what you have. Do what you can. – Arthur Ashe

Don’t stop until you’re proud.

Strength does not come from physical capacity. It comes from an indomitable will. – Mahatma Gandhi

I’m not telling you it is going to be easy, I’m telling you it’s going to be worth it. – Art Williams

If you want it, you’ll find a way. If you don’t, you’ll find an excuse.

Perseverance is the hard work you do after you get tired of doing the hard work you already did. – Newt Gingrich

It is during our darkest moments that we must focus to see the light. — Aristotle Onassis

Perfection is not attainable, but if we chase perfection we can catch excellence. — Vince Lombardi




We may encounter many defeats but we must not be defeated. – Maya Angelou

Strength doesn’t come from what you can do. It comes from overcoming the things you once thought you couldn’t. – Rikki Rogers

He who is not courageous enough to take risks will accomplish nothing in life. – Muhammad Ali

We don’t develop courage by being happy every day. We develop it by surviving difficult times and challenging adversity. – Barbara De Angelis

When you fear your struggles, your struggles consume you. When you face your struggles, you overcome them.

I learned that courage was not the absence of fear, but the triumph over it. The brave man is not he who does not feel afraid, but he who conquers that fear. – Nelson Mandela

Keep going. Everything you need will come to you at the perfect time.

Set a goal so big that you can’t achieve it until you grow into the person who can. – Unknown

All our dreams can come true, if we have the courage to pursue them. – Walt Disney

The path to success is to take massive, determined action. – Tony Robbins

The only person you are destined to become is the person you decide to be. —Ralph Waldo Emerson

If you get tired, learn to rest, not quit.

Pessimism leads to weakness, optimism to power. – William James
'''

ndung='''

1) “The Way Get Started Is To Quit Talking And Begin Doing.” – Walt Disney
2) “The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.” – Winston Churchill
3) “Don’t Let Yesterday Take Up Too Much Of Today.” – Will Rogers
4) “You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.” – Unknown
5) “It’s Not Whether You Get Knocked Down, It’s Whether You Get Up.” – Inspirational Quote By Vince Lombardi
6) “If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You.” – Steve Jobs
7) “People Who Are Crazy Enough To Think They Can Change The World, Are The Ones Who Do.” – Rob Siltanen
8) “Failure Will Never Overtake Me If My Determination To Succeed Is Strong Enough.” – Og Mandino
9) “Entrepreneurs Are Great At Dealing With Uncertainty And Also Very Good At Minimizing Risk. That’s The Classic Entrepreneur.” – Mohnish Pabrai
10) “We May Encounter Many Defeats But We Must Not Be Defeated.” – Maya Angelou
11) “Knowing Is Not Enough; We Must Apply. Wishing Is Not Enough; We Must Do.” – Johann Wolfgang Von Goethe
12) “Imagine Your Life Is Perfect In Every Respect; What Would It Look Like?” – Brian Tracy
13) “We Generate Fears While We Sit. We Overcome Them By Action.” – Dr. Henry Link
14) “Whether You Think You Can Or Think You Can’t, You’re Right.” – Quote By Henry Ford
15) “Security Is Mostly A Superstition. Life Is Either A Daring Adventure Or Nothing.” – Life Quote By Helen Keller
16) “The Man Who Has Confidence In Himself Gains The Confidence Of Others.” – Hasidic Proverb
17) “The Only Limit To Our Realization Of Tomorrow Will Be Our Doubts Of Today.” – Motivational Quote By Franklin D. Roosevelt
18) “Creativity Is Intelligence Having Fun.” – Albert Einstein
19) “What You Lack In Talent Can Be Made Up With Desire, Hustle And Giving 110% All The Time.” – Don Zimmer
20) “Do What You Can With All You Have, Wherever You Are.” – Theodore Roosevelt
21) “Develop An ‘Attitude Of Gratitude’. Say Thank You To Everyone You Meet For Everything They Do For You.” – Encouraging Quote By Brian Tracy
22) “You Are Never Too Old To Set Another Goal Or To Dream A New Dream.” – C.S. Lewis
23) “To See What Is Right And Not Do It Is A Lack Of Courage.” – Confucius
24) “Reading Is To The Mind, As Exercise Is To The Body.” – Brian Tracy
25) “Fake It Until You Make It! Act As If You Had All The Confidence You Require Until It Becomes Your Reality.” – Brian Tracy
26) “The Future Belongs To The Competent. Get Good, Get Better, Be The Best!” – Success Quote By Brian Tracy
27) “For Every Reason It’s Not Possible, There Are Hundreds Of People Who Have Faced The Same Circumstances And Succeeded.” – Jack Canfield
28) “Things Work Out Best For Those Who Make The Best Of How Things Work Out.” – Positive Quote By John Wooden
29) “A Room Without Books Is Like A Body Without A Soul.” – Marcus Tullius Cicero
30) “I Think Goals Should Never Be Easy, They Should Force You To Work, Even If They Are Uncomfortable At The Time.” – Michael Phelps
31) “One Of The Lessons That I Grew Up With Was To Always Stay True To Yourself And Never Let What Somebody Else Says Distract You From Your Goals.” – Michelle Obama
32) “Today’s Accomplishments Were Yesterday’s Impossibilities.” – Robert H. Schuller
33) “The Only Way To Do Great Work Is To Love What You Do. If You Haven’t Found It Yet, Keep Looking. Don’t Settle.” – Steve Jobs
34) “You Don’t Have To Be Great To Start, But You Have To Start To Be Great.” – Zig Ziglar
35)  “A Clear Vision, Backed By Definite Plans, Gives You A Tremendous Feeling Of Confidence And Personal Power.” – Brian Tracy
36) “There Are No Limits To What You Can Accomplish, Except The Limits You Place On Your Own Thinking.” – Brian Tracy
20 Success Quotes For Inspirational Leaders
37) “Integrity Is The Most Valuable And Respected Quality Of Leadership. Always Keep Your Word.”
38) “Leadership Is The Ability To Get Extraordinary Achievement From Ordinary People”
39) “Leaders Set High Standards. Refuse To Tolerate Mediocrity Or Poor Performance”
40) “Clarity Is The Key To Effective Leadership. What Are Your Goals?”
41) “The Best Leaders Have A High Consideration Factor. They Really Care About Their People”
42) “Leaders Think And Talk About The Solutions. Followers Think And Talk About The Problems.”
43) “The Key Responsibility Of Leadership Is To Think About The Future. No One Else Can Do It For You.”
44) “The Effective Leader Recognizes That They Are More Dependent On Their People Than They Are On Them. Walk Softly.”
45) “Leaders Never Use The Word Failure. They Look Upon Setbacks As Learning Experiences.”
46) “Practice Golden Rule Management In Everything You Do. Manage Others The Way You Would Like To Be Managed.”
47) “Superior Leaders Are Willing To Admit A Mistake And Cut Their Losses. Be Willing To Admit That You’ve Changed Your Mind. Don’t Persist When The Original Decision Turns Out To Be A Poor One.”
48) “Leaders Are Anticipatory Thinkers. They Consider All Consequences Of Their Behaviors Before They Act.”
49) “The True Test Of Leadership Is How Well You Function In A Crisis.”
50) “Leaders Concentrate Single-Mindedly On One Thing– The Most Important Thing, And They Stay At It Until It’s Complete.”
51) “The Three ‘C’s’ Of Leadership Are Consideration, Caring, And Courtesy. Be Polite To Everyone.”
52) “Respect Is The Key Determinant Of High-Performance Leadership. How Much People Respect You Determines How Well They Perform.”
53) “Leadership Is More Who You Are Than What You Do.”
54) “Entrepreneurial Leadership Requires The Ability To Move Quickly When Opportunity Presents Itself.”
55) “Leaders Are Innovative, Entrepreneurial, And Future-Oriented. They Focus On Getting The Job Done.”
56) “Leaders Are Never Satisfied; They Continually Strive To Be Better.”
'''
kq=regex1.findall(ndung)
for line in kq:
	print(line)
	#print(line[0])
