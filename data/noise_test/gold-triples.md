## Manually made triples to verify accuracy.

# Context noise tests real facts surrounded by increasing gibberish
# Tests: Can model extract signal from noise? Does it hallucinate from gibberish?
GOLD = {
    "p1.md": [
        ("nikola tesla", "was", "serbian-american inventor"),
        ("nikola tesla", "was", "electrical engineer"),
    ],
    "p2.md": [ 
        ("nikola tesla", "was", "serbian-american inventor"),
        ("nikola tesla", "was", "electrical engineer"),
        ("nikola tesla", "best known for", "developing alternating current electrical system"),
        ("tesla", "held", "over 300 patents"),
    ],
    "p3.md": [ 
        ("nikola tesla", "was", "serbian-american inventor"),
        ("nikola tesla", "was", "electrical engineer"),
        ("nikola tesla", "best known for", "contributions to design of modern ac electricity supply system"),
        ("nikola tesla", "born in", "1856"),
        ("nikola tesla", "born in", "croatia"),
        ("nikola tesla", "studied", "engineering"),
        ("nikola tesla", "studied", "physics"),
        ("nikola tesla", "invented", "numerous devices and technologies"),
    ],
    "p4.md": [  
        ("nikola tesla", "was", "serbian-american inventor"),
        ("nikola tesla", "was", "electrical engineer"),
        ("nikola tesla", "best known for", "contributions to design of modern ac electricity supply system"),
        ("nikola tesla", "born in", "1856"),
        ("nikola tesla", "born in", "croatia"),
        ("nikola tesla", "studied", "engineering"),
        ("nikola tesla", "studied", "physics"),
        ("nikola tesla", "invented", "numerous devices and technologies"),
        ("tesla's inventions", "include", "tesla coil"),
        ("tesla's inventions", "include", "induction motor"),
        ("tesla's inventions", "include", "early radio technology"),
        ("nikola tesla", "died in", "1943"),
    ],
    "p5.md": [ 
        ("nikola tesla", "was", "serbian-american inventor"),
        ("nikola tesla", "was", "electrical engineer"),
        ("nikola tesla", "best known for", "contributions to design of modern ac electricity supply system"),
        ("nikola tesla", "born in", "1856"),
        ("nikola tesla", "born in", "croatia"),
        ("nikola tesla", "studied", "engineering"),
        ("nikola tesla", "studied", "physics"),
        ("nikola tesla", "invented", "numerous devices and technologies"),
        ("tesla's inventions", "include", "tesla coil"),
        ("tesla's inventions", "include", "induction motor"),
        ("tesla's inventions", "include", "early radio technology"),
        ("nikola tesla", "died in", "1943"),
        ("nikola tesla", "known for", "eccentric personality"),
        ("nikola tesla", "known for", "visionary ideas"),
        ("nikola tesla", "experimented with", "wireless transmission of electricity"),
        ("nikola tesla", "celebrated as", "pioneer of electrical engineering"),
    ],
}