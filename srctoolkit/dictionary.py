#!/usr/bin/env python
# -*- encoding: utf-8 -*-


PREPOSITIONS = {
    'from', 'out', 'above', 'up', 'with', 'between', 'besides', 'on', 
    'until', 'beside', 'across', 'behind', 'off', 'near', 'under', 
    'about', 'inside', 'in', 'to', 'against', 'down', 'as', 'throughout', 
    'upon', 'except', 'below', 'outside', 'toward', 'without', 'by', 
    'till', 'of', 'around', 'at', 'through', 'beyond', 'for', 'into', 
    'like', 'over', 'after', 'since', 'before', 'beneath', 'during'
}

PHRASAL_VERBS = {
    "act": {"act out", "act up"},
    "add": {"add on", "add up"},
    "age": {"age out"},
    "arm": {"arm up"},
    "ask": {"ask out"},
    "asphalt": {"asphalt over"},
    "auction": {"auction off"},
    "back": {"back off", "back up"},
    "bad": {"bad off"},
    "bail": {"bail out"},
    "balance": {"balance out"},
    "bandage": {"bandage up"},
    "bandy": {"bandy about", "bandy around"},
    "bang": {"bang on"},
    "bank": {"bank up"},
    "bark": {"bark up the wrong tree"},
    "bash": {"bash up"},
    "bat": {"bat in"},
    "be": {"be all", "be like"},
    "bead": {"bead up"},
    "bear": {"bear down", "bear out", "bear up"},
    "beat": {"beat up", "beat out", "beat down"},
    "bed": {"bed down"},
    "beef": {"beef up"},
    "belch": {"belch out"},
    "belly": {"belly up"},
    "belt": {"belt out"},
    "bind": {"bind up"},
    "black": {"black out"},
    "blast": {"blast off", "blast away"},
    "bleed": {"bleed off", "bleed out"},
    "block": {"block up"},
    "blot": {"blot out"},
    "blow": {"blow up", "blow out", "blow over"},
    "blurt": {"blurt out"},
    "board": {"board up"},
    "bog": {"bog down"},
    "boil": {"boil over", "boil down"},
    "bone": {"bone up"},
    "boob": {"boob out"},
    "book": {"book up"},
    "boom": {"boom out"},
    "boot": {"boot up"},
    "boss": {"boss around"},
    "bottle": {"bottle up"},
    "bottom": {"bottom out"},
    "bounce": {"bounce back"},
    "bound": {"bound up"},
    "bow": {"bow down", "bow out"},
    "bowl": {"bowl over"},
    "box": {"box in"},
    "branch": {"branch out"},
    "brazen": {"brazen out"},
    "break": {"break even", "break through", "break in", "break ground", "break out", "break off", "break up", "break away", "break down"},
    "brick": {"brick over"},
    "bring": {"bring on", "bring up", "bring along", "bring about", "bring down"},
    "broke": {"broke ass"},
    "brush": {"brush up", "brush off"},
    "buck": {"buck up"},
    "buckle": {"buckle down", "buckle up"},
    "build": {"build up"},
    "bump": {"bump off", "bump up"},
    "bunch": {"bunch up"},
    "bundle": {"bundle up"},
    "buoy": {"buoy up"},
    "burn": {"burn up", "burn out"},
    "burst": {"burst out"},
    "bust": {"bust out", "bust up"},
    "butt": {"butt in"},
    "butter": {"butter up"},
    "buy": {"buy out", "buy into", "buy up", "buy off"},
    "buzz": {"buzz off"},
    "call": {"call up", "call out", "call upon", "call off", "call in", "call on"},
    "calm": {"calm down"},
    "camp": {"camp out"},
    "carry": {"carry out", "carry on", "carry off", "carry over"},
    "cart": {"cart off"},
    "carve": {"carve out"},
    "cash": {"cash in"},
    "catch": {"catch on", "catch up"},
    "cave": {"cave in"},
    "chalk": {"chalk up"},
    "charge": {"charge off"},
    "chart": {"chart out"},
    "chatter": {"chatter away"},
    "check": {"check in", "check out", "check up"},
    "cheer": {"cheer up", "cheer on"},
    "cheese": {"cheese off"},
    "chew": {"chew up"},
    "chicken": {"chicken out"},
    "chill": {"chill out"},
    "chip": {"chip in"},
    "choke": {"choke off", "choke up"},
    "chop": {"chop down", "chop up"},
    "clean": {"clean up", "clean out"},
    "clear": {"clear up", "clear out"},
    "clip": {"clip off"},
    "clog": {"clog up"},
    "close": {"close in", "close over", "close up", "close down", "close off"},
    "clown": {"clown around"},
    "clutch": {"clutch on"},
    "coil": {"coil up"},
    "color": {"color in"},
    "come": {"come on", "come out", "come up", "come about", "come off", "come in", "come across", "come through", "come down", "come to", "come along", "come over", "come upon", "come by"},
    "concrete": {"concrete over"},
    "cone": {"cone down"},
    "conference": {"conference in"},
    "conjure": {"conjure up"},
    "contract": {"contract out"},
    "cook": {"cook up"},
    "cool": {"cool off", "cool down"},
    "coop": {"coop up"},
    "copy": {"copy out"},
    "core": {"core out"},
    "cough": {"cough up"},
    "cover": {"cover up", "cover over"},
    "crack": {"crack up", "crack down"},
    "crank": {"crank out", "crank up"},
    "crash": {"crash out"},
    "creep": {"creep up", "creep out"},
    "crisp": {"crisp up"},
    "crop": {"crop up"},
    "cross": {"cross out"},
    "cry": {"cry out", "cry down"},
    "cuban": {"cuban out"},
    "curl": {"curl up"},
    "cut": {"cut out", "cut off", "cut loose", "cut up", "cut down", "cut back"},
    "dash": {"dash off"},
    "deck": {"deck out"},
    "dick": {"dick around"},
    "die": {"die down", "die out", "die off"},
    "dig": {"dig out", "dig up"},
    "dine": {"dine out"},
    "dish": {"dish out", "dish up"},
    "divide": {"divide up"},
    "divvy": {"divvy up"},
    "do": {"do away", "do in"},
    "dole": {"dole out"},
    "doll": {"doll up"},
    "done": {"done for"},
    "dope": {"dope up"},
    "doze": {"doze off"},
    "drag": {"drag on"},
    "draw": {"draw up"},
    "dream": {"dream up", "dream on"},
    "dredge": {"dredge up"},
    "dress": {"dress up", "dress down"},
    "drink": {"drink up"},
    "drop": {"drop by", "drop off", "drop in", "drop out"},
    "drown": {"drown out"},
    "drug": {"drug up"},
    "drum": {"drum up"},
    "dry": {"dry out", "dry up"},
    "dust": {"dust off"},
    "ease": {"ease up"},
    "eat": {"eat away", "eat up"},
    "edge": {"edge out"},
    "egg": {"egg on"},
    "eke": {"eke out"},
    "end": {"end up"},
    "even": {"even out"},
    "face": {"face off"},
    "fall": {"fall apart", "fall over", "fall out", "fall off", "fall back", "fall through"},
    "fap": {"fap away"},
    "farm": {"farm out"},
    "fart": {"fart around"},
    "fatten": {"fatten up"},
    "fed": {"fed up"},
    "feed": {"feed up"},
    "feel": {"feel up"},
    "fence": {"fence off"},
    "fend": {"fend off"},
    "ferret": {"ferret out"},
    "fess": {"fess up"},
    "fight": {"fight on", "fight back", "fight off"},
    "figure": {"figure out"},
    "fill": {"fill in", "fill out", "fill up"},
    "find": {"find out"},
    "finish": {"finish up", "finish off", "finish out"},
    "firm": {"firm up"},
    "fit": {"fit in"},
    "fix": {"fix up"},
    "flake": {"flake out"},
    "flare": {"flare up"},
    "flash": {"flash back"},
    "flatten": {"flatten out"},
    "flesh": {"flesh out"},
    "flip": {"flip out", "flip off"},
    "flush": {"flush out"},
    "fly": {"fly out"},
    "fob": {"fob off"},
    "fold": {"fold up"},
    "follow": {"follow through", "follow up", "follow suit"},
    "fool": {"fool around"},
    "fork": {"fork over", "fork out"},
    "fort": {"fort up"},
    "freak": {"freak out"},
    "free": {"free up"},
    "freeze": {"freeze over"},
    "freshen": {"freshen up"},
    "frighten": {"frighten away", "frighten off"},
    "fritter": {"fritter away"},
    "frost": {"frost up", "frost over"},
    "fuck": {"fuck off", "fuck up", "fuck around"},
    "fudge": {"fudge over"},
    "gang": {"gang up"},
    "gas": {"gas up"},
    "gear": {"gear up"},
    "gen": {"gen up"},
    "get": {"get back", "get off", "get grip", "get along", "get by", "get together", "get through", "get on", "get down", "get even", "get out", "get away", "get up"},
    "give": {"give rise to", "give out", "give back", "give off", "give over", "give in", "give up", "give away"},
    "glass": {"glass over"},
    "glaze": {"glaze over"},
    "gloss": {"gloss over"},
    "go": {"go down", "go back", "go on", "go down on", "go over", "go through", "go off", "go out"},
    "gobble": {"gobble up"},
    "greater": {"greater than symbol"},
    "grind": {"grind up"},
    "grow": {"grow up"},
    "gulp": {"gulp down"},
    "gum": {"gum up"},
    "gun": {"gun down"},
    "hack": {"hack away"},
    "hail": {"hail down"},
    "ham": {"ham up"},
    "hammer": {"hammer out", "hammer away"},
    "hand": {"hand over", "hand out"},
    "hang": {"hang out", "hang on", "hang up"},
    "hard": {"hard put"},
    "hash": {"hash out"},
    "haul": {"haul in", "haul out"},
    "head": {"head off", "head up"},
    "heat": {"heat up"},
    "help": {"help out"},
    "hem": {"hem in"},
    "hide": {"hide out"},
    "hit": {"hit on", "hit up"},
    "hobnob": {"hobnob around"},
    "hold": {"hold out", "hold off", "hold back", "hold up", "hold over", "hold on"},
    "hole": {"hole up"},
    "hollow": {"hollow out"},
    "hook": {"hook up"},
    "hum": {"hum along"},
    "hurry": {"hurry up"},
    "hype": {"hype up"},
    "iron": {"iron out"},
    "jack": {"jack up"},
    "jet": {"jet off"},
    "join": {"join up", "join in"},
    "joke": {"joke around"},
    "jot": {"jot down"},
    "jump": {"jump up", "jump in"},
    "jut": {"jut out"},
    "keep": {"keep on", "keep up"},
    "keg": {"keg stand"},
    "key": {"key in"},
    "kick": {"kick off", "kick in"},
    "kill": {"kill off"},
    "knock": {"knock off", "knock out", "knock over", "knock up", "knock back", "knock down"},
    "laid": {"laid back"},
    "lam": {"lam out"},
    "lash": {"lash out"},
    "latch": {"latch on"},
    "lay": {"lay off", "lay on"},
    "lead": {"lead off", "lead up"},
    "leave": {"leave off", "leave behind", "leave out", "leave over"},
    "let": {"let on", "let up", "let out", "let down"},
    "level": {"level off"},
    "lick": {"lick up"},
    "lie": {"lie down", "lie in"},
    "light": {"light up"},
    "lighten": {"lighten up"},
    "limber": {"limber up"},
    "line": {"line up"},
    "link": {"link up"},
    "live": {"live up", "live on", "live out", "live down"},
    "liven": {"liven up"},
    "load": {"load up"},
    "loan": {"loan out"},
    "lock": {"lock down", "lock up", "lock in", "lock out"},
    "log": {"log off", "log in", "log on", "log out"},
    "look": {"look after", "look down", "look into", "look forward", "look out", "look up", "look over"},
    "loosen": {"loosen up"},
    "lose": {"lose out"},
    "louse": {"louse up"},
    "luck": {"luck out"},
    "make": {"make do", "make out", "make off", "make believe", "make it", "make over", "make up"},
    "mark": {"mark down", "mark up"},
    "marry": {"marry off"},
    "match": {"match up"},
    "max": {"max out"},
    "meet": {"meet up"},
    "mellow": {"mellow out"},
    "melt": {"melt down"},
    "mess": {"mess up"},
    "mete": {"mete out"},
    "mic": {"mic up"},
    "miss": {"miss out"},
    "mist": {"mist up", "mist over"},
    "mix": {"mix up"},
    "monkey": {"monkey around"},
    "move": {"move on"},
    "muck": {"muck up"},
    "muddle": {"muddle up"},
    "nail": {"nail down"},
    "narrow": {"narrow down"},
    "neaten": {"neaten up"},
    "net": {"net out"},
    "nod": {"nod off"},
    "oil": {"oil up"},
    "open": {"open up"},
    "out": {"out trade"},
    "own": {"own up"},
    "pack": {"pack away", "pack up"},
    "pair": {"pair off", "pair up"},
    "palm": {"palm off"},
    "pan": {"pan out"},
    "parcel": {"parcel out"},
    "pare": {"pare down"},
    "pass": {"pass on", "pass up", "pass off", "pass by", "pass away", "pass over", "pass out"},
    "patch": {"patch up"},
    "pay": {"pay off", "pay down", "pay up", "pay out"},
    "peel": {"peel off"},
    "pen": {"pen up"},
    "pension": {"pension off"},
    "pep": {"pep up"},
    "perk": {"perk up"},
    "peter": {"peter out"},
    "phase": {"phase out", "phase in"},
    "pick": {"pick off", "pick out", "pick away", "pick up", "pick on"},
    "pile": {"pile on", "pile up"},
    "pimp": {"pimp out"},
    "pin": {"pin down"},
    "pine": {"pine away"},
    "pipe": {"pipe up", "pipe down"},
    "piss": {"piss off"},
    "pitch": {"pitch in"},
    "play": {"play down", "play up", "play out", "play to", "play on", "play off"},
    "plot": {"plot out"},
    "plug": {"plug in", "plug up"},
    "point": {"point out"},
    "poke": {"poke around"},
    "polish": {"polish up", "polish off"},
    "pony": {"pony up"},
    "poof": {"poof up", "poof out"},
    "pop": {"pop up", "pop off"},
    "pound": {"pound out"},
    "prate": {"prate on"},
    "price": {"price out"},
    "prick": {"prick up"},
    "print": {"print out"},
    "prop": {"prop up"},
    "pucker": {"pucker up"},
    "puff": {"puff up"},
    "puke": {"puke up"},
    "pull": {"pull over", "pull through", "pull down", "pull up", "pull out", "pull off"},
    "pump": {"pump up", "pump out"},
    "push": {"push up"},
    "put": {"put out", "put on", "put up", "put down", "put in", "put off"},
    "puttyduddy": {"puttyduddy around"},
    "putz": {"putz around"},
    "queue": {"queue up"},
    "quiet": {"quiet down"},
    "quieten": {"quieten down"},
    "rack": {"rack up"},
    "rake": {"rake in"},
    "ramp": {"ramp up"},
    "ratchet": {"ratchet up"},
    "ration": {"ration out"},
    "rattle": {"rattle on", "rattle off"},
    "read": {"read off", "read up"},
    "rear": {"rear end"},
    "reel": {"reel off"},
    "rein": {"rein in"},
    "rent": {"rent out"},
    "rev": {"rev up"},
    "ride": {"ride up", "ride out"},
    "rig": {"rig up"},
    "ring": {"ring up"},
    "rip": {"rip off", "rip out", "rip up"},
    "rise": {"rise up"},
    "rock": {"rock on"},
    "roll": {"roll out", "roll back", "roll up"},
    "root": {"root out"},
    "rough": {"rough up", "rough in"},
    "round": {"round up", "round out"},
    "rubber": {"rubber stamp"},
    "rule": {"rule out"},
    "run": {"run up", "run out", "run over", "run off", "run in", "run down"},
    "salt": {"salt away"},
    "save": {"save up"},
    "saw": {"saw up"},
    "scent": {"scent out"},
    "scoop": {"scoop up"},
    "scout": {"scout out"},
    "scratch": {"scratch out"},
    "scrawl": {"scrawl out"},
    "screen": {"screen out"},
    "screw": {"screw over", "screw up"},
    "scrub": {"scrub up"},
    "scrunch": {"scrunch up"},
    "seal": {"seal off"},
    "seek": {"seek out"},
    "seize": {"seize up"},
    "sell": {"sell off", "sell out"},
    "send": {"send out"},
    "serve": {"serve up"},
    "set": {"set off", "set about", "set down", "set up", "set upon", "set forth", "set out"},
    "settle": {"settle down"},
    "sew": {"sew up"},
    "shack": {"shack up"},
    "shake": {"shake up", "shake off"},
    "shape": {"shape up"},
    "share": {"share out"},
    "shell": {"shell out"},
    "shine": {"shine through"},
    "ship": {"ship out"},
    "shoot": {"shoot off", "shoot back", "shoot up", "shoot down"},
    "shore": {"shore up"},
    "shout": {"shout out", "shout down"},
    "show": {"show up", "show off"},
    "shrug": {"shrug off"},
    "shuffle": {"shuffle off"},
    "shut": {"shut down", "shut out", "shut off", "shut up"},
    "shuttle": {"shuttle off"},
    "shy": {"shy away"},
    "sign": {"sign in", "sign off", "sign on", "sign up"},
    "silt": {"silt up"},
    "single": {"single out"},
    "siphon": {"siphon off"},
    "sit": {"sit in", "sit out", "sit down", "sit up"},
    "size": {"size up"},
    "sketch": {"sketch out"},
    "skim": {"skim off"},
    "skip": {"skip off"},
    "slack": {"slack off"},
    "slag": {"slag off"},
    "sleep": {"sleep off", "sleep away", "sleep over"},
    "slice": {"slice up"},
    "slim": {"slim down"},
    "slip": {"slip in"},
    "slough": {"slough off"},
    "slow": {"slow down"},
    "slug": {"slug out"},
    "sluice": {"sluice down"},
    "smarten": {"smarten up"},
    "smash": {"smash up"},
    "smooth": {"smooth over", "smooth out"},
    "snap": {"snap up", "snap off"},
    "snatch": {"snatch away"},
    "sniff": {"sniff out"},
    "snuff": {"snuff out"},
    "soak": {"soak up"},
    "sober": {"sober up"},
    "sock": {"sock away"},
    "sort": {"sort out"},
    "sound": {"sound off"},
    "speak": {"speak out", "speak up", "speak for"},
    "speed": {"speed up"},
    "spell": {"spell out"},
    "spend": {"spend down"},
    "spike": {"spike out"},
    "spill": {"spill out", "spill over"},
    "spin": {"spin off"},
    "splash": {"splash out"},
    "split": {"split up"},
    "spout": {"spout off"},
    "spread": {"spread out"},
    "spring": {"spring up"},
    "spruce": {"spruce up"},
    "square": {"square off"},
    "squeeze": {"squeeze out"},
    "squirrel": {"squirrel away"},
    "stack": {"stack up"},
    "stake": {"stake out"},
    "stall": {"stall out", "stall off"},
    "stamp": {"stamp out"},
    "stand": {"stand by", "stand down", "stand up", "stand out"},
    "stare": {"stare down"},
    "start": {"start off", "start in", "start up", "start over", "start out"},
    "stash": {"stash away"},
    "stave": {"stave off"},
    "stay": {"stay over", "stay on"},
    "steal": {"steal away"},
    "steer": {"steer clear"},
    "step": {"step aside", "step in", "step down", "step up"},
    "stick": {"stick out", "stick around", "stick up"},
    "stiff": {"stiff arm"},
    "stir": {"stir up"},
    "stock": {"stock up"},
    "stop": {"stop up", "stop off", "stop by", "stop over"},
    "store": {"store up"},
    "straighten": {"straighten up", "straighten out"},
    "stress": {"stress out"},
    "stretch": {"stretch out"},
    "strike": {"strike down", "strike up", "strike out"},
    "string": {"string up"},
    "strip": {"strip away"},
    "study": {"study up"},
    "suck": {"suck up"},
    "suit": {"suit up"},
    "sum": {"sum up"},
    "summon": {"summon forth"},
    "swallow": {"swallow up"},
    "swear": {"swear in", "swear off"},
    "sweat": {"sweat off", "sweat out"},
    "sweep": {"sweep up"},
    "switch": {"switch over"},
    "swoop": {"swoop up"},
    "tack": {"tack down", "tack on"},
    "tag": {"tag team", "tag along"},
    "take": {"take hold", "take off", "take away", "take aback", "take down", "take over", "take up", "take out", "take in", "take on"},
    "talk": {"talk out"},
    "tally": {"tally up"},
    "tamp": {"tamp down"},
    "tangle": {"tangle up"},
    "tape": {"tape up"},
    "taper": {"taper off"},
    "tax": {"tax away"},
    "team": {"team up"},
    "tear": {"tear down", "tear up"},
    "tease": {"tease out"},
    "tee": {"tee off"},
    "tell": {"tell on"},
    "thaw": {"thaw out"},
    "thin": {"thin out"},
    "think": {"think through", "think over", "think up"},
    "thrash": {"thrash out"},
    "throw": {"throw in", "throw away", "throw up", "throw out"},
    "tick": {"tick off"},
    "tide": {"tide over"},
    "tidy": {"tidy up"},
    "tie": {"tie down", "tie in", "tie up"},
    "tighten": {"tighten up"},
    "tip": {"tip over", "tip off"},
    "tire": {"tire out"},
    "tone": {"tone down"},
    "tool": {"tool up"},
    "top": {"top out", "top off", "top up"},
    "toss": {"toss in", "toss up", "toss out"},
    "total": {"total up"},
    "totter": {"totter around"},
    "touch": {"touch off", "touch up", "touch on", "touch base", "touch upon"},
    "track": {"track down"},
    "trade": {"trade off", "trade in"},
    "trail": {"trail off"},
    "trigger": {"trigger off"},
    "trim": {"trim down"},
    "trot": {"trot out"},
    "trough": {"trough out"},
    "try": {"try out"},
    "tuck": {"tuck in", "tuck away"},
    "tune": {"tune in", "tune out"},
    "turn": {"turn down", "turn on", "turn away", "turn over", "turn out", "turn off", "turn in", "turn up"},
    "type": {"type up"},
    "up": {"up front"},
    "use": {"use up"},
    "usher": {"usher in"},
    "vamp": {"vamp up"},
    "vomit": {"vomit up"},
    "vote": {"vote down"},
    "wait": {"wait out"},
    "wake": {"wake up"},
    "walk": {"walk in"},
    "wall": {"wall off"},
    "ward": {"ward off"},
    "warm": {"warm over", "warm up"},
    "wash": {"wash up", "wash down"},
    "watch": {"watch out", "watch over"},
    "water": {"water down"},
    "wear": {"wear out", "wear on", "wear down", "wear off"},
    "weasel": {"weasel out"},
    "weigh": {"weigh in"},
    "well": {"well off", "well up"},
    "whack": {"whack off"},
    "while": {"while away"},
    "whip": {"whip out", "whip up"},
    "whittle": {"whittle down"},
    "whiz": {"whiz away"},
    "win": {"win over"},
    "wind": {"wind up", "wind down"},
    "wipe": {"wipe off", "wipe up", "wipe out"},
    "wise": {"wise up"},
    "wolf": {"wolf down"},
    "work": {"work up", "work out"},
    "worked": {"worked up"},
    "wrap": {"wrap up"},
    "wring": {"wring out"},
    "write": {"write up", "write off", "write in", "write down", "write out"},
    "yammer": {"yammer away", "yammer on"},
    "yield": {"yield up"},
    "zero": {"zero in", "zero out"},
    "zip": {"zip up"},
    "zone": {"zone out"},
    "zonked": {"zonked out"},
    "zoom": {"zoom in", "zoom out"},
}

VERB_PATTERN = {
    "test": [
        "with",
        "to",
        "of",
        "for",
        "in"
    ],
    "copy": [
        "to",
        "of",
        "from",
        "with",
        "in"
    ],
    "extend": [
        "to",
        "with",
        "for",
        "down",
        "by"
    ],
    "init": [
        "from",
        "as",
        "for",
        "with",
        "in"
    ],
    "record": [
        "with",
        "to",
        "without",
        "in",
        "on"
    ],
    "accept": [
        "from",
        "with",
        "in",
        "by",
        "of"
    ],
    "add": [
        "to",
        "for",
        "of",
        "in",
        "from"
    ],
    "equal": [
        "to",
        "on",
        "with",
        "in",
        "for"
    ],
    "adjust": [
        "for",
        "to",
        "into",
        "by",
        "of"
    ],
    "decrypt": [
        "with",
        "by",
        "from",
        "to",
        "as"
    ],
    "update": [
        "with",
        "for",
        "from",
        "by",
        "in"
    ],
    "ai": [
        "to"
    ],
    "be": [
        "in",
        "to",
        "for",
        "of",
        "on"
    ],
    "change": [
        "to",
        "from",
        "in",
        "for",
        "by"
    ],
    "order": [
        "by",
        "on",
        "as",
        "for",
        "in"
    ],
    "alter": [
        "at",
        "of",
        "to",
        "by",
        "in"
    ],
    "hash": [
        "of",
        "for",
        "to",
        "with",
        "by"
    ],
    "escape": [
        "for",
        "to",
        "in",
        "as",
        "with"
    ],
    "initialize": [
        "from",
        "for",
        "with",
        "in",
        "as"
    ],
    "decode": [
        "to",
        "from",
        "for",
        "with",
        "as"
    ],
    "encode": [
        "to",
        "as",
        "from",
        "for",
        "into"
    ],
    "assert": [
        "in",
        "of",
        "to",
        "with",
        "on"
    ],
    "get": [
        "for",
        "by",
        "of",
        "from",
        "as"
    ],
    "activate": [
        "on",
        "by",
        "with",
        "in",
        "for"
    ],
    "attempt": [
        "to",
        "in",
        "on",
        "from",
        "with"
    ],
    "find": [
        "by",
        "for",
        "in",
        "with",
        "from"
    ],
    "bug": [
        "around",
        "to"
    ],
    "request": [
        "to",
        "in",
        "for",
        "on",
        "with"
    ],
    "end": [
        "with",
        "of",
        "on",
        "at",
        "in"
    ],
    "abort": [
        "on",
        "with",
        "from",
        "up",
        "in"
    ],
    "enable": [
        "for",
        "with",
        "in",
        "to",
        "on"
    ],
    "abstract": [
        "to",
        "before",
        "for",
        "in",
        "on"
    ],
    "check": [
        "for",
        "in",
        "with",
        "to",
        "out"
    ],
    "account": [
        "in",
        "with",
        "for",
        "before",
        "from"
    ],
    "accumulate": [
        "to",
        "between",
        "until",
        "for",
        "after"
    ],
    "acquire": [
        "by",
        "for",
        "with",
        "from",
        "to"
    ],
    "advise": [
        "by",
        "against",
        "before",
        "in"
    ],
    "perform": [
        "up",
        "with",
        "on",
        "for",
        "in"
    ],
    "burn": [
        "out",
        "in",
        "from"
    ],
    "apply": [
        "to",
        "as",
        "for",
        "with",
        "on"
    ],
    "adapt": [
        "to",
        "for",
        "from",
        "with",
        "by"
    ],
    "scale": [
        "to",
        "by",
        "down",
        "in",
        "for"
    ],
    "suffix": [
        "of",
        "by",
        "for",
        "to",
        "after"
    ],
    "stretch": [
        "to",
        "by"
    ],
    "second": [
        "of",
        "to",
        "as",
        "between",
        "in"
    ],
    "back": [
        "up",
        "off",
        "to",
        "by",
        "in"
    ],
    "advance": [
        "to",
        "by",
        "on",
        "in",
        "of"
    ],
    "token": [
        "to",
        "with",
        "for",
        "on",
        "of"
    ],
    "transform": [
        "to",
        "from",
        "for",
        "with",
        "in"
    ],
    "save": [
        "to",
        "as",
        "in",
        "for",
        "with"
    ],
    "scan": [
        "for",
        "to",
        "with",
        "by",
        "at"
    ],
    "track": [
        "in",
        "with",
        "up",
        "for",
        "from"
    ],
    "sort": [
        "by",
        "in",
        "at",
        "to",
        "with"
    ],
    "file": [
        "to",
        "on",
        "from",
        "with",
        "after"
    ],
    "align": [
        "to",
        "with",
        "in",
        "for",
        "on"
    ],
    "leave": [
        "to",
        "with",
        "from",
        "for",
        "of"
    ],
    "allocate": [
        "for",
        "on",
        "to",
        "with",
        "in"
    ],
    "slow": [
        "down",
        "off",
        "to"
    ],
    "allow": [
        "to",
        "in",
        "for",
        "on",
        "by"
    ],
    "invalid": [
        "in",
        "to",
        "for",
        "by",
        "of"
    ],
    "alternate": [
        "for",
        "with",
        "to"
    ],
    "shift": [
        "of",
        "to",
        "by",
        "for",
        "down"
    ],
    "analyse": [
        "with",
        "at"
    ],
    "analyze": [
        "with",
        "by",
        "in",
        "for",
        "as"
    ],
    "angle": [
        "between",
        "to",
        "on",
        "from",
        "of"
    ],
    "import": [
        "from",
        "with",
        "to",
        "into",
        "as"
    ],
    "predict": [
        "with",
        "by",
        "for",
        "to",
        "on"
    ],
    "drop": [
        "down",
        "to",
        "from",
        "by",
        "for"
    ],
    "long": [
        "to",
        "from",
        "for",
        "at",
        "by"
    ],
    "merge": [
        "from",
        "with",
        "into",
        "to",
        "in"
    ],
    "append": [
        "to",
        "of",
        "with",
        "from",
        "as"
    ],
    "pay": [
        "by",
        "for",
        "off",
        "until",
        "in"
    ],
    "protect": [
        "from",
        "with",
        "in",
        "for",
        "against"
    ],
    "talk": [
        "to",
        "in"
    ],
    "bundle": [
        "to",
        "from",
        "up",
        "for",
        "in"
    ],
    "tag": [
        "to",
        "with",
        "in",
        "as",
        "from"
    ],
    "arrange": [
        "for",
        "by"
    ],
    "create": [
        "from",
        "for",
        "with",
        "to",
        "of"
    ],
    "single": [
        "to",
        "with",
        "from",
        "for",
        "in"
    ],
    "rest": [
        "of",
        "to",
        "down",
        "out",
        "for"
    ],
    "dimension": [
        "from",
        "as",
        "to",
        "at"
    ],
    "load": [
        "from",
        "in",
        "by",
        "to",
        "with"
    ],
    "read": [
        "from",
        "by",
        "to",
        "as",
        "with"
    ],
    "set": [
        "up",
        "on",
        "to",
        "of",
        "in"
    ],
    "store": [
        "to",
        "in",
        "for",
        "as",
        "with"
    ],
    "convert": [
        "to",
        "from",
        "for",
        "in",
        "with"
    ],
    "delete": [
        "with",
        "by",
        "from",
        "on",
        "in"
    ],
    "insert": [
        "before",
        "at",
        "into",
        "after",
        "of"
    ],
    "resize": [
        "for",
        "to",
        "with",
        "of",
        "on"
    ],
    "array": [
        "with",
        "to",
        "of",
        "at",
        "from"
    ],
    "arrow": [
        "down",
        "for"
    ],
    "enter": [
        "in",
        "for",
        "by",
        "with",
        "at"
    ],
    "article": [
        "to",
        "in"
    ],
    "verify": [
        "with",
        "for",
        "in",
        "to",
        "of"
    ],
    "chide": [
        "for"
    ],
    "collapse": [
        "to",
        "from",
        "with",
        "at",
        "before"
    ],
    "click": [
        "on",
        "in",
        "to",
        "by",
        "down"
    ],
    "work": [
        "with",
        "in",
        "for",
        "to",
        "out"
    ],
    "log": [
        "in",
        "out",
        "to",
        "with",
        "for"
    ],
    "expand": [
        "to",
        "with",
        "by",
        "from",
        "for"
    ],
    "ask": [
        "for",
        "to",
        "before",
        "on",
        "about"
    ],
    "assemble": [
        "from",
        "with",
        "to",
        "for",
        "like"
    ],
    "assign": [
        "to",
        "from",
        "as",
        "by",
        "with"
    ],
    "await": [
        "until",
        "down",
        "for",
        "on",
        "with"
    ],
    "start": [
        "with",
        "up",
        "for",
        "from",
        "in"
    ],
    "enqueue": [
        "for",
        "after",
        "up",
        "with",
        "from"
    ],
    "post": [
        "to",
        "on",
        "from",
        "for",
        "with"
    ],
    "put": [
        "in",
        "to",
        "for",
        "with",
        "into"
    ],
    "run": [
        "on",
        "in",
        "with",
        "to",
        "as"
    ],
    "write": [
        "to",
        "as",
        "out",
        "with",
        "by"
    ],
    "attach": [
        "to",
        "for",
        "in",
        "at",
        "on"
    ],
    "attribute": [
        "to",
        "with",
        "for",
        "as",
        "in"
    ],
    "base": [
        "on",
        "for",
        "to",
        "with",
        "of"
    ],
    "format": [
        "to",
        "with",
        "for",
        "as",
        "of"
    ],
    "authenticate": [
        "with",
        "by",
        "for",
        "to",
        "as"
    ],
    "authorize": [
        "for",
        "to",
        "with",
        "in",
        "from"
    ],
    "detect": [
        "with",
        "from",
        "in",
        "on",
        "by"
    ],
    "fit": [
        "in",
        "to",
        "on",
        "into",
        "for"
    ],
    "reverse": [
        "by",
        "up",
        "with",
        "in",
        "for"
    ],
    "blob": [
        "from",
        "with",
        "before",
        "after",
        "in"
    ],
    "cap": [
        "at",
        "to",
        "by",
        "between"
    ],
    "network": [
        "to",
        "for",
        "in",
        "up",
        "down"
    ],
    "use": [
        "for",
        "in",
        "with",
        "as",
        "to"
    ],
    "fetch": [
        "by",
        "from",
        "for",
        "with",
        "into"
    ],
    "open": [
        "for",
        "in",
        "with",
        "from",
        "up"
    ],
    "owl": [
        "to"
    ],
    "compatible": [
        "with"
    ],
    "linear": [
        "to"
    ],
    "translate": [
        "to",
        "from",
        "for",
        "by",
        "with"
    ],
    "kill": [
        "with",
        "in",
        "by",
        "on",
        "out"
    ],
    "begin": [
        "with",
        "in",
        "off",
        "of",
        "by"
    ],
    "blend": [
        "to",
        "with",
        "off",
        "on"
    ],
    "build": [
        "in",
        "from",
        "for",
        "with",
        "to"
    ],
    "boot": [
        "up",
        "from",
        "with",
        "for",
        "in"
    ],
    "intersect": [
        "with",
        "to",
        "by",
        "as",
        "of"
    ],
    "buffer": [
        "to",
        "from",
        "with",
        "until",
        "up"
    ],
    "bulk": [
        "for",
        "to",
        "off",
        "in",
        "by"
    ],
    "bur": [
        "with"
    ],
    "rgb": [
        "to",
        "for",
        "from"
    ],
    "background": [
        "to",
        "at",
        "for",
        "up",
        "near"
    ],
    "balance": [
        "after",
        "by",
        "on",
        "across",
        "in"
    ],
    "object": [
        "to",
        "with",
        "from",
        "in",
        "as"
    ],
    "draw": [
        "on",
        "with",
        "in",
        "to",
        "at"
    ],
    "batch": [
        "with",
        "to",
        "on",
        "of",
        "by"
    ],
    "beat": [
        "out",
        "of",
        "on"
    ],
    "best": [
        "of",
        "for",
        "from",
        "above"
    ],
    "bias": [
        "between",
        "to",
        "from"
    ],
    "byte": [
        "with",
        "to",
        "from",
        "without",
        "in"
    ],
    "character": [
        "to",
        "of",
        "at",
        "for",
        "in"
    ],
    "double": [
        "to",
        "with",
        "on",
        "for",
        "from"
    ],
    "float": [
        "to",
        "of",
        "from",
        "with",
        "at"
    ],
    "integer": [
        "to",
        "from",
        "in",
        "with",
        "for"
    ],
    "list": [
        "with",
        "for",
        "by",
        "to",
        "up"
    ],
    "string": [
        "to",
        "for",
        "from",
        "with",
        "as"
    ],
    "int": [
        "with",
        "between",
        "for"
    ],
    "bin": [
        "to",
        "for"
    ],
    "output": [
        "to",
        "for",
        "with",
        "in",
        "from"
    ],
    "bind": [
        "to",
        "with",
        "as",
        "for",
        "of"
    ],
    "thread": [
        "at",
        "for",
        "on",
        "without",
        "in"
    ],
    "tick": [
        "to",
        "on",
        "down",
        "until"
    ],
    "drawable": [
        "by"
    ],
    "unlock": [
        "after",
        "to",
        "with",
        "for",
        "out"
    ],
    "black": [
        "by",
        "from",
        "to"
    ],
    "blank": [
        "to",
        "before",
        "out"
    ],
    "bleed": [
        "out"
    ],
    "quote": [
        "as",
        "for",
        "with",
        "from",
        "in"
    ],
    "cipher": [
        "for",
        "up",
        "to",
        "in"
    ],
    "body": [
        "as",
        "to",
        "with",
        "of",
        "on"
    ],
    "bottom": [
        "of",
        "up",
        "from"
    ],
    "bounce": [
        "off",
        "out",
        "with"
    ],
    "bracket": [
        "around",
        "in"
    ],
    "break": [
        "down",
        "up",
        "to",
        "on",
        "for"
    ],
    "label": [
        "from",
        "to",
        "of",
        "by",
        "as"
    ],
    "bring": [
        "to",
        "into",
        "down",
        "up",
        "out"
    ],
    "broadcast": [
        "to",
        "with",
        "by",
        "like",
        "in"
    ],
    "sync": [
        "to",
        "with",
        "from",
        "up",
        "on"
    ],
    "web": [
        "up",
        "from",
        "by",
        "to",
        "like"
    ],
    "customize": [
        "up",
        "after",
        "for",
        "on",
        "with"
    ],
    "predefined": [
        "to",
        "from",
        "with",
        "out"
    ],
    "resolve": [
        "to",
        "for",
        "with",
        "from",
        "as"
    ],
    "concat": [
        "with",
        "to",
        "for",
        "by",
        "of"
    ],
    "receive": [
        "from",
        "as",
        "with",
        "on",
        "to"
    ],
    "archive": [
        "for"
    ],
    "call": [
        "on",
        "with",
        "to",
        "in",
        "for"
    ],
    "substring": [
        "after",
        "before",
        "between",
        "from",
        "until"
    ],
    "can": [
        "to",
        "for",
        "up",
        "on",
        "in"
    ],
    "drag": [
        "to",
        "over",
        "down",
        "with",
        "on"
    ],
    "bound": [
        "to",
        "by",
        "as",
        "for",
        "in"
    ],
    "scroll": [
        "to",
        "by",
        "into",
        "down",
        "up"
    ],
    "should": [
        "on",
        "from",
        "to",
        "over",
        "with"
    ],
    "will": [
        "in",
        "to",
        "of",
        "on",
        "up"
    ],
    "cancel": [
        "in",
        "with",
        "for",
        "on",
        "by"
    ],
    "finish": [
        "up",
        "from",
        "with",
        "on",
        "to"
    ],
    "cast": [
        "to",
        "of",
        "with",
        "from",
        "for"
    ],
    "tail": [
        "to",
        "in"
    ],
    "judge": [
        "in"
    ],
    "disable": [
        "for",
        "in",
        "with",
        "on",
        "to"
    ],
    "default": [
        "for",
        "to",
        "of",
        "up",
        "with"
    ],
    "release": [
        "for",
        "to",
        "from",
        "with",
        "after"
    ],
    "retain": [
        "for",
        "with",
        "from",
        "on",
        "after"
    ],
    "present": [
        "with",
        "on",
        "from",
        "in",
        "before"
    ],
    "number": [
        "of",
        "to",
        "in",
        "from",
        "for"
    ],
    "range": [
        "by",
        "to",
        "for",
        "with",
        "between"
    ],
    "invalidate": [
        "on",
        "near",
        "for",
        "in",
        "by"
    ],
    "stop": [
        "in",
        "with",
        "for",
        "on",
        "at"
    ],
    "compare": [
        "to",
        "with",
        "by",
        "for",
        "as"
    ],
    "tip": [
        "for"
    ],
    "rect": [
        "to",
        "into",
        "in",
        "for",
        "on"
    ],
    "layer": [
        "up",
        "to",
        "above",
        "in",
        "at"
    ],
    "replace": [
        "with",
        "in",
        "by",
        "at",
        "for"
    ],
    "dash": [
        "from",
        "to"
    ],
    "display": [
        "in",
        "up",
        "to",
        "for",
        "from"
    ],
    "choose": [
        "for",
        "to",
        "from",
        "with",
        "on"
    ],
    "clear": [
        "for",
        "to",
        "in",
        "on",
        "from"
    ],
    "describe": [
        "in",
        "to",
        "for",
        "by",
        "as"
    ],
    "destroy": [
        "by",
        "in",
        "on",
        "for",
        "with"
    ],
    "flush": [
        "to",
        "on",
        "before",
        "with",
        "in"
    ],
    "point": [
        "in",
        "to",
        "on",
        "at",
        "from"
    ],
    "parent": [
        "of",
        "until",
        "to",
        "with",
        "for"
    ],
    "notify": [
        "of",
        "on",
        "about",
        "for",
        "up"
    ],
    "clamp": [
        "to",
        "in"
    ],
    "classify": [
        "to",
        "with",
        "from",
        "as",
        "by"
    ],
    "clip": [
        "to",
        "by",
        "out",
        "with",
        "down"
    ],
    "clock": [
        "to",
        "on",
        "in"
    ],
    "reduce": [
        "to",
        "by",
        "with",
        "on",
        "from"
    ],
    "cmp": [
        "to"
    ],
    "zero": [
        "out",
        "with",
        "in",
        "to",
        "for"
    ],
    "locate": [
        "in",
        "for",
        "by",
        "with",
        "after"
    ],
    "cod": [
        "to",
        "from",
        "with",
        "after"
    ],
    "privilege": [
        "with",
        "from",
        "on",
        "without",
        "to"
    ],
    "user": [
        "out",
        "with"
    ],
    "compile": [
        "to",
        "with",
        "from",
        "for",
        "as"
    ],
    "complement": [
        "of",
        "in",
        "for",
        "with"
    ],
    "compose": [
        "with",
        "by",
        "for",
        "of",
        "from"
    ],
    "connect": [
        "to",
        "with",
        "by",
        "in",
        "from"
    ],
    "core": [
        "in",
        "to",
        "for",
        "at",
        "with"
    ],
    "counter": [
        "to",
        "for",
        "by",
        "from",
        "as"
    ],
    "upload": [
        "to",
        "from",
        "with",
        "in",
        "by"
    ],
    "cull": [
        "to",
        "with",
        "from",
        "by"
    ],
    "launch": [
        "with",
        "from",
        "on",
        "in",
        "for"
    ],
    "cluster": [
        "with",
        "in",
        "for",
        "to",
        "up"
    ],
    "derive": [
        "from",
        "for",
        "with",
        "of",
        "on"
    ],
    "encrypt": [
        "with",
        "by",
        "to",
        "in",
        "for"
    ],
    "finalize": [
        "to",
        "in",
        "for",
        "before",
        "on"
    ],
    "generate": [
        "for",
        "from",
        "with",
        "to",
        "on"
    ],
    "pin": [
        "to",
        "of",
        "by",
        "at",
        "in"
    ],
    "sign": [
        "in",
        "up",
        "out",
        "with",
        "by"
    ],
    "recover": [
        "from",
        "with",
        "to",
        "after",
        "for"
    ],
    "unwrap": [
        "with",
        "to",
        "as",
        "for",
        "from"
    ],
    "wait": [
        "for",
        "until",
        "to",
        "on",
        "till"
    ],
    "look": [
        "up",
        "by",
        "for",
        "at",
        "like"
    ],
    "cache": [
        "for",
        "in",
        "on",
        "up",
        "to"
    ],
    "center": [
        "on",
        "inside",
        "in",
        "from",
        "of"
    ],
    "line": [
        "to",
        "of",
        "in",
        "at",
        "for"
    ],
    "hint": [
        "for",
        "before",
        "with"
    ],
    "hook": [
        "up",
        "to",
        "in",
        "before"
    ],
    "calculate": [
        "for",
        "of",
        "in",
        "from",
        "to"
    ],
    "switch": [
        "to",
        "on",
        "off",
        "out",
        "from"
    ],
    "render": [
        "at",
        "to",
        "as",
        "with",
        "from"
    ],
    "wrap": [
        "as",
        "in",
        "with",
        "up",
        "to"
    ],
    "canonicalize": [
        "for",
        "up",
        "with"
    ],
    "reply": [
        "to",
        "with",
        "in"
    ],
    "cascade": [
        "to",
        "for",
        "after",
        "before",
        "on"
    ],
    "fold": [
        "in",
        "to",
        "until",
        "with",
        "without"
    ],
    "catch": [
        "up",
        "of",
        "by",
        "out",
        "with"
    ],
    "cause": [
        "by",
        "to",
        "of",
        "at",
        "without"
    ],
    "close": [
        "on",
        "for",
        "with",
        "to",
        "after"
    ],
    "free": [
        "to",
        "with",
        "for",
        "after",
        "in"
    ],
    "str": [
        "to",
        "from",
        "in",
        "with"
    ],
    "certificate": [
        "to",
        "with",
        "for",
        "up",
        "from"
    ],
    "channel": [
        "for",
        "to",
        "up",
        "in",
        "without"
    ],
    "char": [
        "at",
        "to",
        "out",
        "from",
        "in"
    ],
    "remove": [
        "from",
        "by",
        "at",
        "for",
        "on"
    ],
    "select": [
        "by",
        "with",
        "on",
        "from",
        "for"
    ],
    "clean": [
        "up",
        "on",
        "after",
        "for",
        "by"
    ],
    "send": [
        "to",
        "with",
        "on",
        "as",
        "for"
    ],
    "clone": [
        "with",
        "from",
        "as",
        "for",
        "in"
    ],
    "distance": [
        "to",
        "from",
        "for",
        "between",
        "of"
    ],
    "pair": [
        "in",
        "by",
        "to",
        "with"
    ],
    "cloud": [
        "to",
        "with",
        "without"
    ],
    "complete": [
        "with",
        "in",
        "of",
        "after",
        "for"
    ],
    "query": [
        "for",
        "by",
        "with",
        "to",
        "as"
    ],
    "collect": [
        "from",
        "for",
        "with",
        "to",
        "by"
    ],
    "collide": [
        "with",
        "for"
    ],
    "colocate": [
        "with"
    ],
    "combine": [
        "with",
        "to",
        "by",
        "as",
        "of"
    ],
    "command": [
        "to",
        "for",
        "out",
        "with",
        "from"
    ],
    "roll": [
        "up",
        "to",
        "on",
        "out",
        "with"
    ],
    "comment": [
        "on",
        "after",
        "before",
        "from",
        "for"
    ],
    "compact": [
        "with",
        "on",
        "for",
        "in",
        "by"
    ],
    "elapse": [
        "since",
        "to",
        "for",
        "before",
        "in"
    ],
    "compress": [
        "to",
        "with",
        "of",
        "by",
        "from"
    ],
    "filter": [
        "by",
        "to",
        "with",
        "out",
        "for"
    ],
    "compute": [
        "for",
        "to",
        "of",
        "from",
        "in"
    ],
    "concatenate": [
        "with",
        "to",
        "by",
        "for",
        "into"
    ],
    "confirm": [
        "up",
        "in",
        "as",
        "to",
        "with"
    ],
    "conform": [
        "to"
    ],
    "mpeg": [
        "to"
    ],
    "con": [
        "to"
    ],
    "construct": [
        "from",
        "to",
        "with",
        "for",
        "as"
    ],
    "delegate": [
        "to",
        "of",
        "for",
        "with"
    ],
    "throw": [
        "on",
        "for",
        "with",
        "of",
        "as"
    ],
    "consume": [
        "to",
        "from",
        "until",
        "with",
        "in"
    ],
    "contact": [
        "up",
        "for",
        "with"
    ],
    "contain": [
        "in",
        "of",
        "with",
        "at",
        "for"
    ],
    "continue": [
        "on",
        "with",
        "after",
        "in",
        "as"
    ],
    "mean": [
        "for",
        "of",
        "by",
        "in",
        "from"
    ],
    "control": [
        "in",
        "for",
        "by",
        "with",
        "down"
    ],
    "name": [
        "for",
        "with",
        "from",
        "in",
        "on"
    ],
    "copyright": [
        "into"
    ],
    "interpolate": [
        "at",
        "out",
        "of",
        "for",
        "between"
    ],
    "cost": [
        "to",
        "of"
    ],
    "crawl": [
        "in",
        "at",
        "from",
        "for",
        "inside"
    ],
    "queue": [
        "for",
        "to",
        "of",
        "up",
        "by"
    ],
    "link": [
        "to",
        "with",
        "for",
        "from",
        "in"
    ],
    "do": [
        "in",
        "with",
        "as",
        "on",
        "up"
    ],
    "show": [
        "up",
        "in",
        "to",
        "for",
        "on"
    ],
    "crop": [
        "to",
        "with",
        "outside",
        "for",
        "from"
    ],
    "cross": [
        "for",
        "over",
        "as",
        "with",
        "up"
    ],
    "support": [
        "in",
        "by",
        "across",
        "with",
        "for"
    ],
    "tilt": [
        "down",
        "up"
    ],
    "move": [
        "to",
        "up",
        "down",
        "from",
        "in"
    ],
    "cut": [
        "off",
        "out",
        "to",
        "from",
        "by"
    ],
    "search": [
        "for",
        "by",
        "in",
        "with",
        "from"
    ],
    "prepare": [
        "for",
        "to",
        "from",
        "with",
        "in"
    ],
    "prune": [
        "to",
        "for",
        "around",
        "by",
        "after"
    ],
    "execute": [
        "with",
        "for",
        "on",
        "in",
        "after"
    ],
    "touch": [
        "up",
        "in",
        "down",
        "to",
        "inside"
    ],
    "debug": [
        "with",
        "on",
        "to",
        "out",
        "for"
    ],
    "mask": [
        "as",
        "with",
        "in",
        "out",
        "to"
    ],
    "visit": [
        "to",
        "in",
        "as",
        "for",
        "up"
    ],
    "go": [
        "to",
        "down",
        "up",
        "in",
        "from"
    ],
    "disjoint": [
        "with",
        "above",
        "below"
    ],
    "parse": [
        "from",
        "to",
        "with",
        "for",
        "as"
    ],
    "validate": [
        "with",
        "for",
        "in",
        "on",
        "to"
    ],
    "date": [
        "in",
        "with",
        "to",
        "for",
        "on"
    ],
    "dot": [
        "for",
        "to",
        "as",
        "before",
        "at"
    ],
    "undo": [
        "to",
        "for",
        "in",
        "after",
        "on"
    ],
    "trigger": [
        "on",
        "with",
        "for",
        "by",
        "after"
    ],
    "abandon": [
        "on",
        "for"
    ],
    "disconnect": [
        "from",
        "on",
        "by",
        "except",
        "in"
    ],
    "keep": [
        "on",
        "in",
        "with",
        "without",
        "after"
    ],
    "reconnect": [
        "to",
        "in",
        "after",
        "on",
        "as"
    ],
    "serialize": [
        "to",
        "with",
        "as",
        "in",
        "for"
    ],
    "deactivate": [
        "from",
        "with",
        "up",
        "for",
        "in"
    ],
    "listen": [
        "to",
        "on",
        "for",
        "with",
        "in"
    ],
    "letter": [
        "to",
        "after",
        "up",
        "at"
    ],
    "deallocate": [
        "for",
        "with",
        "on",
        "before"
    ],
    "decompose": [
        "by",
        "into",
        "in",
        "without"
    ],
    "decompress": [
        "to",
        "by",
        "with",
        "for",
        "after"
    ],
    "download": [
        "to",
        "from",
        "in",
        "with",
        "by"
    ],
    "decrease": [
        "by",
        "of",
        "in",
        "beneath",
        "with"
    ],
    "defect": [
        "inside"
    ],
    "defer": [
        "on",
        "for",
        "after",
        "of",
        "to"
    ],
    "define": [
        "up",
        "in",
        "for",
        "by",
        "to"
    ],
    "enclose": [
        "by",
        "in",
        "with",
        "to",
        "of"
    ],
    "implement": [
        "by",
        "to",
        "on",
        "without",
        "as"
    ],
    "modify": [
        "since",
        "by",
        "in",
        "for",
        "to"
    ],
    "synchronize": [
        "with",
        "to",
        "on",
        "from",
        "for"
    ],
    "declare": [
        "in",
        "of",
        "on",
        "at",
        "for"
    ],
    "deflate": [
        "to"
    ],
    "invoice": [
        "to"
    ],
    "recur": [
        "from",
        "down",
        "with"
    ],
    "demo": [
        "in"
    ],
    "demote": [
        "as",
        "to",
        "from"
    ],
    "depend": [
        "on",
        "by",
        "with",
        "of",
        "upon"
    ],
    "deposit": [
        "except"
    ],
    "deprecate": [
        "to",
        "for",
        "since",
        "with",
        "from"
    ],
    "sound": [
        "off",
        "on",
        "for"
    ],
    "detach": [
        "from",
        "off",
        "at",
        "for",
        "on"
    ],
    "determine": [
        "to",
        "for",
        "from",
        "of",
        "by"
    ],
    "bucket": [
        "to",
        "for",
        "by",
        "from",
        "before"
    ],
    "cpu": [
        "with",
        "over",
        "to",
        "from"
    ],
    "play": [
        "as",
        "from",
        "on",
        "at",
        "to"
    ],
    "process": [
        "to",
        "in",
        "for",
        "from",
        "with"
    ],
    "redo": [
        "to",
        "with",
        "for"
    ],
    "digest": [
        "to",
        "as",
        "of",
        "down",
        "with"
    ],
    "sum": [
        "of",
        "for",
        "by",
        "to",
        "up"
    ],
    "dim": [
        "above",
        "of",
        "from",
        "through",
        "without"
    ],
    "direct": [
        "by",
        "for",
        "from",
        "on",
        "down"
    ],
    "motion": [
        "to"
    ],
    "disallow": [
        "to",
        "at",
        "in",
        "for",
        "of"
    ],
    "discard": [
        "to",
        "for",
        "on",
        "with",
        "from"
    ],
    "discover": [
        "with",
        "for",
        "of",
        "from",
        "by"
    ],
    "disk": [
        "of",
        "in",
        "up",
        "down",
        "with"
    ],
    "dismiss": [
        "up",
        "to",
        "on",
        "down",
        "by"
    ],
    "dispatch": [
        "on",
        "to",
        "as",
        "in",
        "before"
    ],
    "lose": [
        "on",
        "to",
        "during",
        "after",
        "by"
    ],
    "dispose": [
        "with",
        "of",
        "up",
        "before",
        "out"
    ],
    "distribute": [
        "to",
        "by",
        "with",
        "for",
        "in"
    ],
    "divide": [
        "to",
        "by",
        "of",
        "in",
        "into"
    ],
    "document": [
        "to",
        "about",
        "as",
        "from",
        "with"
    ],
    "expire": [
        "after",
        "at",
        "in",
        "from",
        "to"
    ],
    "lock": [
        "for",
        "by",
        "out",
        "with",
        "on"
    ],
    "doze": [
        "for"
    ],
    "dp": [
        "to"
    ],
    "match": [
        "with",
        "in",
        "to",
        "by",
        "on"
    ],
    "drain": [
        "to",
        "from",
        "in",
        "after",
        "for"
    ],
    "drive": [
        "for",
        "before",
        "to",
        "from"
    ],
    "reason": [
        "to",
        "for",
        "of",
        "with"
    ],
    "enumerate": [
        "in",
        "for",
        "by",
        "to"
    ],
    "make": [
        "from",
        "for",
        "with",
        "up",
        "to"
    ],
    "dummy": [
        "for",
        "with",
        "of"
    ],
    "dump": [
        "to",
        "as",
        "in",
        "with",
        "out"
    ],
    "duplicate": [
        "for",
        "in",
        "to",
        "with",
        "from"
    ],
    "throttle": [
        "with",
        "for",
        "in",
        "on"
    ],
    "edge": [
        "from",
        "to",
        "of",
        "out",
        "into"
    ],
    "effect": [
        "for",
        "of",
        "into"
    ],
    "emit": [
        "off",
        "to",
        "on",
        "with",
        "in"
    ],
    "report": [
        "to",
        "on",
        "after",
        "for",
        "as"
    ],
    "enum": [
        "to",
        "from",
        "of",
        "with",
        "out"
    ],
    "expect": [
        "at",
        "in",
        "for",
        "to",
        "of"
    ],
    "pronounce": [
        "at"
    ],
    "ease": [
        "in",
        "out",
        "to"
    ],
    "longitude": [
        "to",
        "with"
    ],
    "echo": [
        "in",
        "to",
        "without",
        "with"
    ],
    "reach": [
        "to",
        "from",
        "with"
    ],
    "edit": [
        "to",
        "at",
        "in",
        "of",
        "by"
    ],
    "reflect": [
        "with",
        "as",
        "on",
        "in",
        "from"
    ],
    "seek": [
        "to",
        "after",
        "before",
        "in",
        "inside"
    ],
    "terminate": [
        "with",
        "in",
        "on",
        "by",
        "after"
    ],
    "email": [
        "to",
        "for",
        "from"
    ],
    "embed": [
        "at",
        "to",
        "in",
        "into",
        "with"
    ],
    "empty": [
        "to",
        "with",
        "as",
        "of",
        "for"
    ],
    "feature": [
        "to",
        "from",
        "of",
        "at",
        "up"
    ],
    "initial": [
        "for",
        "with",
        "to",
        "off",
        "up"
    ],
    "encounter": [
        "with"
    ],
    "enforce": [
        "on",
        "of",
        "for",
        "in",
        "before"
    ],
    "enhance": [
        "for",
        "from",
        "with"
    ],
    "ensure": [
        "in",
        "for",
        "of",
        "on",
        "up"
    ],
    "full": [
        "to",
        "up",
        "for",
        "as",
        "on"
    ],
    "err": [
        "out",
        "to",
        "with",
        "as",
        "from"
    ],
    "occur": [
        "between",
        "after",
        "on",
        "of",
        "in"
    ],
    "estimate": [
        "for",
        "from",
        "of",
        "in",
        "since"
    ],
    "evaluate": [
        "to",
        "as",
        "with",
        "in",
        "on"
    ],
    "even": [
        "after",
        "to",
        "before",
        "from",
        "up"
    ],
    "export": [
        "to",
        "as",
        "with",
        "by",
        "for"
    ],
    "subscribe": [
        "to",
        "with",
        "for",
        "on",
        "from"
    ],
    "exact": [
        "of",
        "up",
        "at"
    ],
    "except": [
        "to"
    ],
    "exchange": [
        "for",
        "from",
        "down"
    ],
    "exclude": [
        "from",
        "with",
        "for",
        "by",
        "to"
    ],
    "exist": [
        "in",
        "with",
        "by",
        "for",
        "on"
    ],
    "exit": [
        "for",
        "with",
        "by",
        "in",
        "on"
    ],
    "expense": [
        "from"
    ],
    "conflict": [
        "with",
        "in"
    ],
    "key": [
        "to",
        "at",
        "for",
        "up",
        "down"
    ],
    "value": [
        "of",
        "at",
        "for",
        "with",
        "from"
    ],
    "extract": [
        "from",
        "to",
        "for",
        "as",
        "with"
    ],
    "extrapolate": [
        "from",
        "by"
    ],
    "verbose": [
        "up",
        "to"
    ],
    "eye": [
        "up"
    ],
    "face": [
        "to",
        "of",
        "from",
        "for",
        "down"
    ],
    "fail": [
        "to",
        "on",
        "with",
        "at",
        "of"
    ],
    "interfere": [
        "by",
        "with"
    ],
    "resume": [
        "with",
        "at",
        "on",
        "after",
        "from"
    ],
    "fan": [
        "in",
        "out",
        "to"
    ],
    "fast": [
        "to",
        "for",
        "by",
        "from",
        "out"
    ],
    "publish": [
        "to",
        "with",
        "in",
        "from",
        "on"
    ],
    "fill": [
        "in",
        "with",
        "from",
        "up",
        "to"
    ],
    "film": [
        "in"
    ],
    "ignore": [
        "for",
        "of",
        "in",
        "by",
        "from"
    ],
    "fix": [
        "up",
        "to",
        "for",
        "from",
        "after"
    ],
    "fpr": [
        "to"
    ],
    "purge": [
        "from",
        "with",
        "on",
        "for",
        "before"
    ],
    "reload": [
        "from",
        "on",
        "in",
        "for",
        "to"
    ],
    "reset": [
        "to",
        "in",
        "for",
        "with",
        "from"
    ],
    "restart": [
        "with",
        "from",
        "in",
        "on",
        "at"
    ],
    "factorize": [
        "with"
    ],
    "fade": [
        "out",
        "in",
        "to",
        "from",
        "after"
    ],
    "must": [
        "on"
    ],
    "deploy": [
        "with",
        "to",
        "on",
        "in",
        "from"
    ],
    "specify": [
        "in",
        "with",
        "by",
        "to",
        "for"
    ],
    "trust": [
        "from",
        "to",
        "on",
        "of",
        "since"
    ],
    "fake": [
        "by",
        "before",
        "in",
        "for",
        "up"
    ],
    "saturate": [
        "by"
    ],
    "fence": [
        "off",
        "in"
    ],
    "detail": [
        "to"
    ],
    "transfer": [
        "to",
        "in",
        "from",
        "for",
        "after"
    ],
    "split": [
        "by",
        "to",
        "into",
        "at",
        "on"
    ],
    "fine": [
        "with",
        "at"
    ],
    "fingerprint": [
        "for",
        "to"
    ],
    "fire": [
        "on",
        "up",
        "to",
        "before",
        "in"
    ],
    "major": [
        "to",
        "from"
    ],
    "flash": [
        "to",
        "on",
        "off",
        "for",
        "with"
    ],
    "flatten": [
        "to",
        "as",
        "with",
        "into",
        "at"
    ],
    "climb": [
        "up"
    ],
    "flip": [
        "to",
        "on",
        "for",
        "around",
        "over"
    ],
    "need": [
        "to",
        "for",
        "after",
        "up",
        "with"
    ],
    "focus": [
        "on",
        "in",
        "out",
        "to",
        "after"
    ],
    "follow": [
        "up",
        "by",
        "in",
        "to",
        "with"
    ],
    "force": [
        "to",
        "at",
        "as",
        "on",
        "for"
    ],
    "forget": [
        "in",
        "after",
        "for",
        "from"
    ],
    "form": [
        "in",
        "to",
        "with",
        "from",
        "below"
    ],
    "forward": [
        "to",
        "on",
        "for",
        "in",
        "as"
    ],
    "from": [
        "from",
        "to"
    ],
    "frame": [
        "of",
        "to",
        "from",
        "in",
        "by"
    ],
    "fulfill": [
        "in"
    ],
    "function": [
        "with",
        "in",
        "as",
        "up",
        "by"
    ],
    "rescale": [
        "to",
        "for",
        "on",
        "with"
    ],
    "input": [
        "to",
        "from",
        "for",
        "about",
        "on"
    ],
    "size": [
        "of",
        "to",
        "with",
        "in",
        "from"
    ],
    "plan": [
        "from",
        "for",
        "to",
        "before",
        "of"
    ],
    "last": [
        "of",
        "up",
        "in",
        "with",
        "for"
    ],
    "push": [
        "to",
        "down",
        "in",
        "for",
        "by"
    ],
    "zip": [
        "with",
        "to",
        "up",
        "from",
        "through"
    ],
    "gpr": [
        "to"
    ],
    "require": [
        "for",
        "by",
        "with",
        "in",
        "to"
    ],
    "factor": [
        "for",
        "with",
        "to",
        "out",
        "from"
    ],
    "increase": [
        "by",
        "to",
        "of",
        "in",
        "off"
    ],
    "gain": [
        "from",
        "by",
        "of",
        "with",
        "to"
    ],
    "game": [
        "over",
        "up",
        "with",
        "by",
        "of"
    ],
    "garage": [
        "at"
    ],
    "shut": [
        "down",
        "on",
        "with",
        "in",
        "for"
    ],
    "populate": [
        "from",
        "for",
        "with",
        "in",
        "to"
    ],
    "general": [
        "of",
        "to",
        "for",
        "with",
        "without"
    ],
    "return": [
        "for",
        "to",
        "with",
        "of",
        "from"
    ],
    "short": [
        "to"
    ],
    "handle": [
        "in",
        "to",
        "up",
        "with",
        "for"
    ],
    "net": [
        "without",
        "from"
    ],
    "monitor": [
        "in",
        "from",
        "to",
        "for",
        "on"
    ],
    "like": [
        "like",
        "with"
    ],
    "pause": [
        "for",
        "with",
        "after",
        "between",
        "on"
    ],
    "give": [
        "with",
        "to",
        "up",
        "of",
        "by"
    ],
    "turing": [
        "with"
    ],
    "google": [
        "to",
        "around"
    ],
    "goto": [
        "in",
        "of",
        "with",
        "across",
        "from"
    ],
    "grade": [
        "for",
        "in"
    ],
    "refresh": [
        "on",
        "from",
        "with",
        "at",
        "in"
    ],
    "graph": [
        "to",
        "from",
        "on",
        "with",
        "in"
    ],
    "triple": [
        "to",
        "as",
        "of",
        "for"
    ],
    "restore": [
        "from",
        "to",
        "in",
        "up",
        "on"
    ],
    "gray": [
        "to",
        "for",
        "out"
    ],
    "spy": [
        "on",
        "for"
    ],
    "grind": [
        "to",
        "of"
    ],
    "group": [
        "by",
        "between",
        "for",
        "to",
        "in"
    ],
    "guard": [
        "with",
        "for",
        "by"
    ],
    "have": [
        "in",
        "to",
        "of",
        "for",
        "at"
    ],
    "heap": [
        "to",
        "down",
        "up"
    ],
    "hsb": [
        "to"
    ],
    "hand": [
        "over",
        "to",
        "in",
        "with",
        "into"
    ],
    "stack": [
        "to",
        "as",
        "in",
        "of",
        "with"
    ],
    "head": [
        "for",
        "with",
        "of",
        "to",
        "at"
    ],
    "hex": [
        "to",
        "of",
        "after",
        "from"
    ],
    "hide": [
        "up",
        "from",
        "on",
        "in",
        "for"
    ],
    "level": [
        "up",
        "from"
    ],
    "word": [
        "in"
    ],
    "highlight": [
        "in",
        "with",
        "after",
        "as",
        "from"
    ],
    "sin": [
        "to",
        "from"
    ],
    "mount": [
        "from",
        "on",
        "in",
        "out",
        "to"
    ],
    "pose": [
        "with",
        "as",
        "out",
        "from",
        "to"
    ],
    "hold": [
        "in",
        "out",
        "by",
        "on",
        "off"
    ],
    "hole": [
        "of"
    ],
    "home": [
        "by",
        "for"
    ],
    "hop": [
        "to"
    ],
    "host": [
        "to",
        "with",
        "for",
        "on",
        "by"
    ],
    "circle": [
        "to",
        "down",
        "up",
        "for",
        "on"
    ],
    "hue": [
        "of",
        "to"
    ],
    "spell": [
        "with",
        "out"
    ],
    "stem": [
        "as"
    ],
    "suggest": [
        "as",
        "for",
        "to",
        "on",
        "with"
    ],
    "identify": [
        "by",
        "with",
        "from",
        "as",
        "to"
    ],
    "install": [
        "on",
        "from",
        "in",
        "to",
        "as"
    ],
    "invert": [
        "from",
        "for",
        "with",
        "to"
    ],
    "master": [
        "with",
        "for",
        "to",
        "on"
    ],
    "probe": [
        "for",
        "up",
        "to",
        "in",
        "out"
    ],
    "speed": [
        "up",
        "to",
        "of"
    ],
    "iso": [
        "to"
    ],
    "miss": [
        "in",
        "at",
        "on",
        "with",
        "to"
    ],
    "delay": [
        "to",
        "by",
        "in",
        "for",
        "after"
    ],
    "shape": [
        "of",
        "to",
        "for",
        "in",
        "around"
    ],
    "idle": [
        "in",
        "between",
        "for"
    ],
    "promise": [
        "of"
    ],
    "true": [
        "to",
        "of",
        "for"
    ],
    "associate": [
        "with",
        "to",
        "by",
        "from",
        "for"
    ],
    "improve": [
        "to"
    ],
    "include": [
        "in",
        "for",
        "by",
        "with",
        "from"
    ],
    "answer": [
        "on",
        "out",
        "in",
        "to",
        "by"
    ],
    "index": [
        "of",
        "to",
        "for",
        "by",
        "in"
    ],
    "infer": [
        "from",
        "to",
        "of",
        "for",
        "by"
    ],
    "infix": [
        "to"
    ],
    "inflate": [
        "from",
        "with",
        "for",
        "to"
    ],
    "inform": [
        "about",
        "of",
        "from",
        "upon",
        "up"
    ],
    "inhibit": [
        "until"
    ],
    "card": [
        "to",
        "at",
        "in",
        "of",
        "like"
    ],
    "inject": [
        "into",
        "with",
        "at",
        "on",
        "to"
    ],
    "skip": [
        "to",
        "until",
        "of",
        "for",
        "in"
    ],
    "inset": [
        "for"
    ],
    "instance": [
        "of",
        "from",
        "for",
        "to",
        "with"
    ],
    "instantiate": [
        "with",
        "in",
        "from",
        "to",
        "for"
    ],
    "integrate": [
        "by",
        "with",
        "in",
        "across",
        "to"
    ],
    "inter": [
        "on"
    ],
    "rotate": [
        "to",
        "by",
        "around",
        "with",
        "in"
    ],
    "zoom": [
        "out",
        "in",
        "to",
        "from",
        "by"
    ],
    "interleave": [
        "to",
        "with",
        "at",
        "on",
        "from"
    ],
    "introduce": [
        "in",
        "to",
        "for"
    ],
    "introspect": [
        "for",
        "with",
        "up",
        "to"
    ],
    "mix": [
        "with",
        "in",
        "into",
        "up",
        "over"
    ],
    "sub": [
        "to",
        "for",
        "of",
        "as",
        "in"
    ],
    "invite": [
        "to",
        "by",
        "without",
        "in"
    ],
    "invoke": [
        "on",
        "with",
        "for",
        "after",
        "in"
    ],
    "interrupt": [
        "by",
        "on",
        "up",
        "for",
        "in"
    ],
    "press": [
        "in",
        "with",
        "down",
        "for",
        "until"
    ],
    "revoke": [
        "for",
        "from",
        "in",
        "with",
        "on"
    ],
    "train": [
        "on",
        "with",
        "at",
        "from",
        "till"
    ],
    "capitalize": [
        "with",
        "in",
        "as"
    ],
    "intercept": [
        "before",
        "off",
        "to",
        "with",
        "on"
    ],
    "iterate": [
        "to",
        "over",
        "by",
        "with",
        "for"
    ],
    "jar": [
        "of",
        "without",
        "in"
    ],
    "configure": [
        "for",
        "from",
        "with",
        "in",
        "as"
    ],
    "register": [
        "for",
        "out",
        "with",
        "on",
        "in"
    ],
    "indent": [
        "with",
        "after",
        "in",
        "out",
        "to"
    ],
    "map": [
        "to",
        "from",
        "with",
        "by",
        "as"
    ],
    "flow": [
        "through",
        "to",
        "from",
        "with",
        "into"
    ],
    "jabber": [
        "to"
    ],
    "impl": [
        "on",
        "to",
        "as",
        "by",
        "with"
    ],
    "job": [
        "to",
        "in",
        "with",
        "up",
        "like"
    ],
    "join": [
        "with",
        "on",
        "to",
        "as",
        "from"
    ],
    "justify": [
        "to"
    ],
    "kick": [
        "from",
        "off",
        "on",
        "out"
    ],
    "dist": [
        "to",
        "from",
        "with"
    ],
    "square": [
        "to",
        "down",
        "at",
        "by",
        "of"
    ],
    "normalize": [
        "to",
        "for",
        "with",
        "in",
        "from"
    ],
    "lch": [
        "to"
    ],
    "mock": [
        "with",
        "for",
        "up",
        "to",
        "in"
    ],
    "leap": [
        "to",
        "on",
        "in"
    ],
    "pass": [
        "to",
        "for",
        "through",
        "as",
        "in"
    ],
    "offset": [
        "to",
        "by",
        "as",
        "at",
        "from"
    ],
    "opt": [
        "out",
        "in",
        "from",
        "to",
        "off"
    ],
    "print": [
        "to",
        "on",
        "out",
        "with",
        "for"
    ],
    "strip": [
        "from",
        "to",
        "for",
        "out",
        "off"
    ],
    "ll": [
        "to"
    ],
    "parallel": [
        "to",
        "of",
        "for",
        "from",
        "with"
    ],
    "lower": [
        "of",
        "to",
        "by",
        "at",
        "with"
    ],
    "pad": [
        "with",
        "to",
        "for",
        "at",
        "after"
    ],
    "result": [
        "to",
        "for",
        "from",
        "by",
        "in"
    ],
    "solve": [
        "in",
        "with",
        "to",
        "without",
        "for"
    ],
    "lv03": [
        "to"
    ],
    "latitude": [
        "to",
        "with",
        "from"
    ],
    "lead": [
        "to",
        "on"
    ],
    "leak": [
        "to",
        "about",
        "in",
        "for",
        "on"
    ],
    "learn": [
        "with",
        "without",
        "by",
        "from",
        "about"
    ],
    "limit": [
        "to",
        "of",
        "by",
        "into",
        "in"
    ],
    "tan": [
        "to"
    ],
    "license": [
        "for"
    ],
    "light": [
        "with",
        "into",
        "down",
        "up",
        "out"
    ],
    "phase": [
        "to",
        "up",
        "at",
        "from"
    ],
    "stable": [
        "in",
        "to"
    ],
    "overflow": [
        "in",
        "on",
        "to"
    ],
    "thumb": [
        "of",
        "to"
    ],
    "low": [
        "down",
        "to"
    ],
    "mat": [
        "to"
    ],
    "mime": [
        "from",
        "for",
        "to",
        "of",
        "with"
    ],
    "mob": [
        "to"
    ],
    "reshape": [
        "to",
        "down",
        "in"
    ],
    "slice": [
        "to",
        "from",
        "for",
        "of",
        "as"
    ],
    "shallow": [
        "of",
        "from",
        "to",
        "without",
        "out"
    ],
    "state": [
        "into",
        "to",
        "with",
        "from",
        "for"
    ],
    "forecast": [
        "at",
        "from"
    ],
    "receipt": [
        "for"
    ],
    "machine": [
        "from"
    ],
    "lot": [
        "of"
    ],
    "treat": [
        "as",
        "on",
        "like",
        "off"
    ],
    "manage": [
        "by",
        "for",
        "with",
        "of",
        "in"
    ],
    "span": [
        "with",
        "by",
        "to",
        "of",
        "from"
    ],
    "mark": [
        "as",
        "for",
        "up",
        "down",
        "to"
    ],
    "multiply": [
        "by",
        "to",
        "in",
        "from",
        "at"
    ],
    "overlap": [
        "with",
        "by",
        "at",
        "in",
        "on"
    ],
    "maximize": [
        "in",
        "with"
    ],
    "rewrite": [
        "to",
        "from",
        "with",
        "for",
        "in"
    ],
    "measure": [
        "for",
        "of",
        "with",
        "before",
        "out"
    ],
    "middle": [
        "down",
        "of"
    ],
    "cover": [
        "by",
        "from",
        "to",
        "of",
        "for"
    ],
    "sleep": [
        "for",
        "at",
        "until",
        "between",
        "with"
    ],
    "mine": [
        "in"
    ],
    "minimize": [
        "with",
        "of",
        "to",
        "for"
    ],
    "model": [
        "to",
        "with",
        "for",
        "from",
        "like"
    ],
    "mother": [
        "of"
    ],
    "motor": [
        "to"
    ],
    "route": [
        "to",
        "with",
        "for",
        "on",
        "as"
    ],
    "murmur": [
        "to"
    ],
    "pick": [
        "up",
        "from",
        "at",
        "by",
        "for"
    ],
    "arch": [
        "to"
    ],
    "trace": [
        "with",
        "for",
        "in",
        "of",
        "from"
    ],
    "parameterized": [
        "with",
        "for",
        "in",
        "by"
    ],
    "pop": [
        "up",
        "from",
        "to",
        "as",
        "for"
    ],
    "serve": [
        "for",
        "as",
        "up",
        "to",
        "in"
    ],
    "alt": [
        "to",
        "off",
        "down",
        "up",
        "on"
    ],
    "narrow": [
        "by",
        "to",
        "of",
        "for"
    ],
    "navigate": [
        "to",
        "up",
        "in",
        "from",
        "through"
    ],
    "negate": [
        "without",
        "except",
        "in"
    ],
    "negotiate": [
        "with",
        "in",
        "without",
        "to"
    ],
    "neighbor": [
        "down",
        "up",
        "for",
        "in",
        "across"
    ],
    "access": [
        "after",
        "from",
        "at",
        "through",
        "for"
    ],
    "context": [
        "for"
    ],
    "root": [
        "to",
        "for",
        "in",
        "of",
        "with"
    ],
    "server": [
        "as",
        "down",
        "from",
        "on"
    ],
    "page": [
        "in",
        "for",
        "by",
        "with",
        "down"
    ],
    "top": [
        "of",
        "down",
        "to",
        "by",
        "on"
    ],
    "one": [
        "of"
    ],
    "power": [
        "of",
        "off",
        "on",
        "to",
        "by"
    ],
    "step": [
        "into",
        "over",
        "in",
        "out",
        "on"
    ],
    "poll": [
        "for",
        "from",
        "to",
        "at",
        "as"
    ],
    "block": [
        "on",
        "with",
        "for",
        "by",
        "until"
    ],
    "literal": [
        "of"
    ],
    "note": [
        "off",
        "on",
        "to",
        "in",
        "with"
    ],
    "nanos": [
        "to"
    ],
    "fall": [
        "to",
        "through",
        "on",
        "off",
        "of"
    ],
    "recognize": [
        "with",
        "in",
        "as",
        "for"
    ],
    "operate": [
        "on",
        "in",
        "by",
        "with",
        "to"
    ],
    "optimize": [
        "for",
        "in",
        "from",
        "by",
        "after"
    ],
    "conn": [
        "to",
        "out",
        "in",
        "for"
    ],
    "fax": [
        "for"
    ],
    "outline": [
        "of"
    ],
    "overlay": [
        "in",
        "on"
    ],
    "own": [
        "by",
        "in",
        "with",
        "up"
    ],
    "win": [
        "in",
        "for",
        "with",
        "to"
    ],
    "patch": [
        "with",
        "from",
        "to",
        "for",
        "as"
    ],
    "bond": [
        "with",
        "to"
    ],
    "php": [
        "for"
    ],
    "plane": [
        "to"
    ],
    "pod": [
        "of"
    ],
    "star": [
        "to",
        "by",
        "in"
    ],
    "paint": [
        "to",
        "for",
        "of",
        "up",
        "on"
    ],
    "paragraph": [
        "by",
        "into"
    ],
    "partition": [
        "by",
        "to",
        "with",
        "for",
        "on"
    ],
    "paste": [
        "from",
        "on",
        "to",
        "into",
        "without"
    ],
    "peak": [
        "without"
    ],
    "peek": [
        "at",
        "from",
        "as",
        "until",
        "near"
    ],
    "peer": [
        "to",
        "like",
        "in"
    ],
    "deny": [
        "in",
        "on",
        "to",
        "with",
        "for"
    ],
    "grant": [
        "to",
        "on",
        "from",
        "for",
        "with"
    ],
    "phone": [
        "with"
    ],
    "right": [
        "to",
        "at",
        "before",
        "in",
        "after"
    ],
    "picture": [
        "from",
        "at",
        "for",
        "to"
    ],
    "tile": [
        "to",
        "at",
        "with",
        "in",
        "from"
    ],
    "place": [
        "at",
        "by",
        "on",
        "in",
        "of"
    ],
    "plain": [
        "with",
        "to",
        "of",
        "for"
    ],
    "plug": [
        "in",
        "for",
        "to",
        "from",
        "into"
    ],
    "position": [
        "from",
        "with",
        "at",
        "after",
        "for"
    ],
    "predicate": [
        "for",
        "with",
        "in",
        "to",
        "from"
    ],
    "prefer": [
        "by",
        "over",
        "to",
        "with",
        "from"
    ],
    "prevent": [
        "to",
        "by",
        "in",
        "for",
        "on"
    ],
    "deal": [
        "with",
        "to",
        "on",
        "for",
        "down"
    ],
    "prim": [
        "as",
        "below",
        "for",
        "at"
    ],
    "profile": [
        "to",
        "from",
        "on",
        "with",
        "at"
    ],
    "program": [
        "out",
        "over",
        "in",
        "for",
        "to"
    ],
    "promote": [
        "to",
        "for",
        "as",
        "from",
        "up"
    ],
    "prompt": [
        "for",
        "to",
        "with",
        "about",
        "in"
    ],
    "propagate": [
        "to",
        "from",
        "down",
        "of",
        "at"
    ],
    "reserve": [
        "for",
        "on",
        "with",
        "in",
        "up"
    ],
    "bypass": [
        "for"
    ],
    "pt": [
        "to",
        "in",
        "between"
    ],
    "pulse": [
        "from"
    ],
    "py": [
        "from"
    ],
    "signal": [
        "on",
        "of",
        "down",
        "to",
        "for"
    ],
    "warn": [
        "with",
        "on",
        "about",
        "out",
        "for"
    ],
    "remainder": [
        "of",
        "by",
        "down",
        "up",
        "for"
    ],
    "subtract": [
        "to",
        "from",
        "in",
        "with",
        "as"
    ],
    "unpack": [
        "from",
        "to",
        "in",
        "of"
    ],
    "time": [
        "out",
        "in",
        "down",
        "from",
        "after"
    ],
    "unicode": [
        "from",
        "as",
        "with",
        "for"
    ],
    "adressing": [
        "after"
    ],
    "quarter": [
        "to",
        "for",
        "as",
        "until"
    ],
    "quit": [
        "in",
        "on",
        "for",
        "to"
    ],
    "ray": [
        "to"
    ],
    "reject": [
        "with",
        "on",
        "without",
        "to",
        "by"
    ],
    "c3": [
        "to"
    ],
    "round": [
        "to",
        "up",
        "down",
        "of",
        "out"
    ],
    "rtf": [
        "to"
    ],
    "radio": [
        "with",
        "in",
        "under",
        "to",
        "off"
    ],
    "raise": [
        "to",
        "on",
        "for",
        "by",
        "out"
    ],
    "rank": [
        "by",
        "of",
        "from",
        "on"
    ],
    "dial": [
        "by"
    ],
    "hang": [
        "up",
        "with",
        "on"
    ],
    "die": [
        "with",
        "in",
        "on"
    ],
    "ready": [
        "for",
        "to",
        "near",
        "in"
    ],
    "view": [
        "to",
        "up",
        "down",
        "for",
        "of"
    ],
    "rebuild": [
        "from",
        "in",
        "up",
        "for",
        "to"
    ],
    "recalculate": [
        "in",
        "of",
        "at",
        "for",
        "to"
    ],
    "recipient": [
        "with"
    ],
    "reconcile": [
        "to",
        "with",
        "in"
    ],
    "reconstruct": [
        "from",
        "for",
        "to"
    ],
    "recreate": [
        "with",
        "in",
        "from",
        "for",
        "on"
    ],
    "recurse": [
        "to",
        "on",
        "over",
        "up"
    ],
    "recycle": [
        "on",
        "from",
        "at",
        "by",
        "up"
    ],
    "redirect": [
        "to",
        "for",
        "as",
        "by",
        "from"
    ],
    "redraw": [
        "outside",
        "to",
        "from",
        "in"
    ],
    "book": [
        "for",
        "to",
        "of",
        "about"
    ],
    "async": [
        "on",
        "in",
        "with",
        "to"
    ],
    "regenerate": [
        "with",
        "of",
        "from",
        "by"
    ],
    "reinitialize": [
        "from",
        "with"
    ],
    "relax": [
        "with",
        "in"
    ],
    "rename": [
        "to",
        "on",
        "with",
        "for",
        "in"
    ],
    "reopen": [
        "by",
        "for",
        "after",
        "at",
        "with"
    ],
    "reorder": [
        "to",
        "by",
        "for",
        "before",
        "with"
    ],
    "repeat": [
        "on",
        "until",
        "for",
        "with",
        "of"
    ],
    "repost": [
        "by"
    ],
    "restrict": [
        "to",
        "by",
        "in",
        "of",
        "for"
    ],
    "retire": [
        "by",
        "with",
        "to"
    ],
    "retrace": [
        "from"
    ],
    "retrieve": [
        "by",
        "from",
        "with",
        "for",
        "as"
    ],
    "retry": [
        "on",
        "up",
        "with",
        "to",
        "after"
    ],
    "reveal": [
        "in",
        "on",
        "of",
        "up",
        "to"
    ],
    "revert": [
        "to",
        "from",
        "with",
        "by",
        "during"
    ],
    "rip": [
        "up"
    ],
    "room": [
        "with",
        "by",
        "for",
        "to",
        "from"
    ],
    "row": [
        "to",
        "from",
        "at",
        "with",
        "for"
    ],
    "sample": [
        "from",
        "to",
        "at",
        "without",
        "with"
    ],
    "relate": [
        "to",
        "by",
        "with",
        "for"
    ],
    "satisfy": [
        "by",
        "with",
        "of",
        "from",
        "as"
    ],
    "see": [
        "in",
        "at",
        "by",
        "on",
        "to"
    ],
    "segment": [
        "for",
        "to",
        "at",
        "after",
        "until"
    ],
    "sha256a": [
        "to"
    ],
    "sha256": [
        "to"
    ],
    "browse": [
        "for",
        "to",
        "from",
        "by",
        "up"
    ],
    "ship": [
        "to",
        "at"
    ],
    "ski": [
        "in"
    ],
    "tap": [
        "with",
        "at",
        "on",
        "to",
        "from"
    ],
    "sock": [
        "for"
    ],
    "sql": [
        "to",
        "for",
        "from",
        "like",
        "with"
    ],
    "simplify": [
        "as",
        "to",
        "from",
        "inside",
        "by"
    ],
    "sse": [
        "to"
    ],
    "renegotiate": [
        "on"
    ],
    "inch": [
        "to"
    ],
    "succeed": [
        "with",
        "in",
        "for",
        "without",
        "to"
    ],
    "recompile": [
        "with",
        "on"
    ],
    "sit": [
        "down",
        "to",
        "out",
        "in",
        "up"
    ],
    "say": [
        "to",
        "by"
    ],
    "scan100": [
        "with"
    ],
    "capture": [
        "out",
        "to",
        "with",
        "in",
        "from"
    ],
    "schedule": [
        "at",
        "with",
        "for",
        "to",
        "in"
    ],
    "screen": [
        "to",
        "on",
        "off",
        "with",
        "out"
    ],
    "cp": [
        "after",
        "like",
        "to"
    ],
    "secure": [
        "for",
        "by",
        "off",
        "on",
        "in"
    ],
    "seed": [
        "from",
        "for",
        "by",
        "with"
    ],
    "sweep": [
        "to"
    ],
    "sentence": [
        "to",
        "with",
        "on"
    ],
    "trip": [
        "on",
        "below"
    ],
    "service": [
        "by",
        "to",
        "in",
        "up",
        "as"
    ],
    "sex": [
        "to"
    ],
    "shadow": [
        "from",
        "by",
        "to"
    ],
    "shake": [
        "to"
    ],
    "share": [
        "with",
        "to",
        "by",
        "in",
        "on"
    ],
    "shrink": [
        "to",
        "until",
        "for",
        "after",
        "from"
    ],
    "shuffle": [
        "in",
        "with",
        "to",
        "of"
    ],
    "shutter": [
        "to"
    ],
    "type": [
        "from",
        "to",
        "with",
        "for",
        "in"
    ],
    "silence": [
        "in",
        "about"
    ],
    "scavenge": [
        "before"
    ],
    "site": [
        "up",
        "with",
        "to",
        "into",
        "for"
    ],
    "smart": [
        "after",
        "to"
    ],
    "smile": [
        "for"
    ],
    "smoke": [
        "with"
    ],
    "rule": [
        "for",
        "to",
        "out",
        "with",
        "without"
    ],
    "source": [
        "to",
        "for",
        "as",
        "from",
        "with"
    ],
    "spawn": [
        "in",
        "at",
        "for",
        "from",
        "as"
    ],
    "speak": [
        "for",
        "by",
        "with",
        "from"
    ],
    "spin": [
        "for",
        "by",
        "at",
        "to",
        "from"
    ],
    "splice": [
        "from",
        "out",
        "to",
        "into",
        "at"
    ],
    "stage": [
        "from",
        "in",
        "to",
        "with",
        "up"
    ],
    "fault": [
        "in",
        "for",
        "from"
    ],
    "still": [
        "in"
    ],
    "null": [
        "to",
        "in",
        "with",
        "on",
        "for"
    ],
    "stream": [
        "to",
        "by",
        "with",
        "in",
        "out"
    ],
    "stress": [
        "up"
    ],
    "stride": [
        "of",
        "in"
    ],
    "strike": [
        "for",
        "by",
        "out"
    ],
    "subject": [
        "with",
        "to",
        "from",
        "like",
        "out"
    ],
    "submit": [
        "to",
        "with",
        "on",
        "by",
        "for"
    ],
    "summarize": [
        "for",
        "with"
    ],
    "surface": [
        "up",
        "at",
        "of",
        "to"
    ],
    "swagger": [
        "with"
    ],
    "swap": [
        "for",
        "with",
        "out",
        "in",
        "to"
    ],
    "interface": [
        "down",
        "up"
    ],
    "swing": [
        "to"
    ],
    "synthesize": [
        "to",
        "from",
        "with"
    ],
    "exceed": [
        "with",
        "without",
        "out",
        "of",
        "off"
    ],
    "tdt": [
        "to"
    ],
    "try": [
        "to",
        "from",
        "for",
        "with",
        "in"
    ],
    "transpose": [
        "for",
        "in",
        "into",
        "by"
    ],
    "trap": [
        "to"
    ],
    "trim": [
        "to",
        "from",
        "by",
        "for",
        "at"
    ],
    "take": [
        "from",
        "until",
        "for",
        "in",
        "with"
    ],
    "target": [
        "of",
        "to",
        "for",
        "with",
        "by"
    ],
    "task": [
        "for",
        "like",
        "to",
        "in",
        "after"
    ],
    "tell": [
        "to",
        "about"
    ],
    "term": [
        "of",
        "for",
        "in",
        "up"
    ],
    "exile": [
        "by",
        "with"
    ],
    "freeze": [
        "at",
        "to"
    ],
    "thin": [
        "out",
        "up",
        "at",
        "to"
    ],
    "nest": [
        "in",
        "with",
        "by",
        "as",
        "inside"
    ],
    "toast": [
        "on"
    ],
    "toggle": [
        "with",
        "in",
        "on",
        "off",
        "up"
    ],
    "tootle": [
        "up"
    ],
    "total": [
        "of",
        "for",
        "in",
        "by",
        "with"
    ],
    "trade": [
        "between",
        "for",
        "to"
    ],
    "transcribe": [
        "for"
    ],
    "transit": [
        "to",
        "at",
        "from"
    ],
    "traverse": [
        "outside",
        "to",
        "down",
        "from",
        "by"
    ],
    "triangulate": [
        "to",
        "at"
    ],
    "truncate": [
        "to",
        "with",
        "at",
        "in",
        "before"
    ],
    "tweet": [
        "with"
    ],
    "void": [
        "with",
        "in",
        "by",
        "to",
        "of"
    ],
    "code": [
        "on"
    ],
    "unbind": [
        "from",
        "up",
        "on",
        "at",
        "with"
    ],
    "unblock": [
        "for",
        "up",
        "from",
        "to",
        "on"
    ],
    "underline": [
        "to"
    ],
    "underscore": [
        "to"
    ],
    "uniform": [
        "to",
        "for",
        "off"
    ],
    "unload": [
        "from",
        "in",
        "into",
        "for",
        "on"
    ],
    "unregister": [
        "for",
        "on",
        "in",
        "from",
        "with"
    ],
    "upgrade": [
        "to",
        "from",
        "for",
        "with",
        "as"
    ],
    "cart": [
        "to",
        "with"
    ],
    "voice": [
        "over"
    ],
    "manifest": [
        "as",
        "to",
        "in"
    ],
    "instal": [
        "by",
        "since",
        "for",
        "from",
        "of"
    ],
    "seat": [
        "to"
    ],
    "stand": [
        "by",
        "on",
        "to",
        "for",
        "from"
    ],
    "mesh": [
        "to",
        "from",
        "up"
    ],
    "mismatch": [
        "in"
    ],
    "constrain": [
        "to",
        "by",
        "in",
        "as",
        "with"
    ],
    "vibrate": [
        "with",
        "to"
    ],
    "chat": [
        "with",
        "on",
        "to",
        "as"
    ],
    "meter": [
        "to",
        "from"
    ],
    "wave": [
        "to",
        "from",
        "in"
    ],
    "wrong": [
        "in",
        "with",
        "for",
        "by",
        "of"
    ],
    "wake": [
        "up",
        "on",
        "in",
        "to",
        "by"
    ],
    "walk": [
        "in",
        "on",
        "to",
        "at",
        "through"
    ],
    "warp": [
        "down",
        "up",
        "to"
    ],
    "watch": [
        "for",
        "on",
        "to",
        "at",
        "down"
    ],
    "weight": [
        "of",
        "to",
        "by",
        "for",
        "in"
    ],
    "white": [
        "to"
    ],
    "withdraw": [
        "to",
        "by",
        "with"
    ],
    "witness": [
        "in"
    ],
    "xml": [
        "to",
        "with",
        "without"
    ],
    "dirty": [
        "from",
        "by",
        "with",
        "on",
        "after"
    ],
    "propogate": [
        "to"
    ],
    "may": [
        "with"
    ],
    "perf": [
        "with",
        "on",
        "to"
    ],
    "coerce": [
        "to",
        "from",
        "for"
    ],
    "soup": [
        "to",
        "by",
        "with"
    ],
    "zap": [
        "to",
        "up"
    ],
    "inherit": [
        "from",
        "on",
        "with",
        "by",
        "through"
    ],
    "par": [
        "with",
        "to",
        "in",
        "out"
    ],
    "aggregate": [
        "by",
        "in",
        "with",
        "for",
        "out"
    ],
    "field": [
        "with"
    ],
    "bean": [
        "to",
        "of",
        "for",
        "from",
        "with"
    ],
    "bump": [
        "up",
        "to",
        "into",
        "for"
    ],
    "claim": [
        "by",
        "with",
        "out",
        "in",
        "for"
    ],
    "rev": [
        "to"
    ],
    "shop": [
        "for"
    ],
    "combat": [
        "out",
        "at",
        "on",
        "with"
    ],
    "commit": [
        "with",
        "to",
        "on",
        "for",
        "in"
    ],
    "consider": [
        "as",
        "for",
        "with",
        "upon",
        "under"
    ],
    "database": [
        "with",
        "from",
        "up"
    ],
    "curve": [
        "to",
        "through",
        "into",
        "from"
    ],
    "dequeue": [
        "up",
        "for",
        "to"
    ],
    "deserialize": [
        "from",
        "with",
        "into",
        "to",
        "as"
    ],
    "chunk": [
        "to",
        "from"
    ],
    "orient": [
        "to",
        "about",
        "by"
    ],
    "dt": [
        "from"
    ],
    "review": [
        "for",
        "by"
    ],
    "ecef": [
        "to"
    ],
    "before": [
        "before"
    ],
    "endpoint": [
        "for",
        "as",
        "in",
        "with",
        "to"
    ],
    "erase": [
        "to",
        "of",
        "from",
        "up",
        "until"
    ],
    "happen": [
        "in",
        "before",
        "of",
        "with",
        "after"
    ],
    "prepend": [
        "to",
        "before",
        "with",
        "at",
        "after"
    ],
    "pointer": [
        "down",
        "up"
    ],
    "intern": [
        "in"
    ],
    "grab": [
        "until",
        "with",
        "of"
    ],
    "compound": [
        "to"
    ],
    "indices": [
        "from",
        "to",
        "in",
        "with"
    ],
    "layout": [
        "with",
        "after"
    ],
    "fraction": [
        "to",
        "of",
        "above",
        "below",
        "by"
    ],
    "tree": [
        "to",
        "for",
        "up",
        "with"
    ],
    "realize": [
        "with",
        "by"
    ],
    "decorate": [
        "with",
        "by",
        "for",
        "down",
        "from"
    ],
    "mapper": [
        "with",
        "for"
    ],
    "marshal": [
        "to",
        "from",
        "as",
        "with",
        "without"
    ],
    "iterator": [
        "from"
    ],
    "relationship": [
        "on"
    ],
    "sequence": [
        "to"
    ],
    "existent": [
        "as"
    ],
    "override": [
        "in",
        "with",
        "of",
        "for",
        "from"
    ],
    "pango": [
        "from",
        "to"
    ],
    "peel": [
        "off",
        "of"
    ],
    "recall": [
        "to",
        "as",
        "of"
    ],
    "repair": [
        "after",
        "before",
        "with",
        "as",
        "on"
    ],
    "replicate": [
        "to",
        "after",
        "with",
        "from",
        "out"
    ],
    "reschedule": [
        "out",
        "in",
        "for",
        "from",
        "to"
    ],
    "reuse": [
        "for",
        "after",
        "in",
        "as",
        "out"
    ],
    "spill": [
        "to",
        "over",
        "in"
    ],
    "suppress": [
        "by",
        "on",
        "after",
        "in",
        "to"
    ],
    "tear": [
        "down",
        "after",
        "for",
        "before",
        "up"
    ],
    "correlate": [
        "in",
        "with",
        "by",
        "to"
    ],
    "collocate": [
        "with"
    ],
    "repaint": [
        "in",
        "down"
    ],
    "title": [
        "of"
    ],
    "widen": [
        "to",
        "by"
    ],
    "yield": [
        "from",
        "to",
        "for"
    ],
    "a1d": [
        "to"
    ],
    "bytes": [
        "to",
        "as",
        "with"
    ],
    "abbreviate": [
        "for"
    ],
    "meet": [
        "for",
        "by",
        "at",
        "with",
        "in"
    ],
    "box": [
        "to"
    ],
    "pan": [
        "to",
        "by",
        "down",
        "up"
    ],
    "absolutize": [
        "against"
    ],
    "absorb": [
        "from",
        "to",
        "by"
    ],
    "initialise": [
        "for",
        "to",
        "in",
        "from",
        "with"
    ],
    "know": [
        "to",
        "in",
        "for",
        "about",
        "by"
    ],
    "abucoins": [
        "for"
    ],
    "bits": [
        "to",
        "on"
    ],
    "acc": [
        "for"
    ],
    "response": [
        "from",
        "out",
        "of",
        "with"
    ],
    "pending": [
        "for",
        "to",
        "in",
        "with",
        "as"
    ],
    "offer": [
        "to",
        "for",
        "from",
        "below",
        "with"
    ],
    "ball": [
        "on",
        "to"
    ],
    "condition": [
        "on",
        "from",
        "of"
    ],
    "achieve": [
        "with"
    ],
    "bolt": [
        "from"
    ],
    "ack": [
        "from",
        "with",
        "on"
    ],
    "mention": [
        "in",
        "as"
    ],
    "acknowledge": [
        "up",
        "by",
        "for",
        "with"
    ],
    "appear": [
        "in",
        "at",
        "to",
        "on",
        "before"
    ],
    "acl": [
        "in",
        "to"
    ],
    "act": [
        "on",
        "like",
        "in",
        "as",
        "with"
    ],
    "pull": [
        "from",
        "up",
        "to",
        "down",
        "by"
    ],
    "flex": [
        "by"
    ],
    "initiate": [
        "out",
        "by",
        "on",
        "with",
        "down"
    ],
    "ping": [
        "for",
        "with",
        "by",
        "from",
        "up"
    ],
    "produce": [
        "of",
        "for",
        "in",
        "to",
        "from"
    ],
    "malformed": [
        "for",
        "under",
        "as",
        "with"
    ],
    "rout": [
        "for",
        "to",
        "with",
        "up",
        "in"
    ],
    "belong": [
        "to",
        "of"
    ],
    "native": [
        "with"
    ],
    "bag": [
        "from",
        "with"
    ],
    "exec": [
        "to"
    ],
    "persist": [
        "to",
        "with",
        "on",
        "as",
        "in"
    ],
    "adb": [
        "up"
    ],
    "carry": [
        "over",
        "on",
        "to",
        "with",
        "out"
    ],
    "advertise": [
        "after"
    ],
    "affect": [
        "by",
        "in",
        "on",
        "without"
    ],
    "animate": [
        "to",
        "by",
        "in",
        "out",
        "from"
    ],
    "constraint": [
        "on",
        "without"
    ],
    "score": [
        "of",
        "for",
        "with",
        "from",
        "inside"
    ],
    "provide": [
        "for",
        "to",
        "by",
        "in",
        "from"
    ],
    "obtain": [
        "for",
        "from",
        "up",
        "to",
        "of"
    ],
    "event": [
        "for",
        "with",
        "before"
    ],
    "joint": [
        "to",
        "from"
    ],
    "case": [
        "to",
        "with",
        "in",
        "on"
    ],
    "overwrite": [
        "by",
        "at",
        "in",
        "during",
        "with"
    ],
    "pool": [
        "to",
        "on",
        "by",
        "with",
        "for"
    ],
    "explode": [
        "on"
    ],
    "coordinate": [
        "to",
        "in",
        "from",
        "with",
        "for"
    ],
    "snapshot": [
        "in"
    ],
    "donate": [
        "on"
    ],
    "evict": [
        "from",
        "in",
        "to",
        "near",
        "on"
    ],
    "reindex": [
        "since"
    ],
    "chain": [
        "with",
        "of",
        "after",
        "on",
        "to"
    ],
    "project": [
        "with",
        "from",
        "by",
        "to",
        "without"
    ],
    "fee": [
        "to",
        "with",
        "from",
        "of",
        "into"
    ],
    "fuse": [
        "into",
        "to"
    ],
    "crash": [
        "at",
        "in",
        "on",
        "for",
        "by"
    ],
    "http": [
        "to",
        "in",
        "for",
        "with"
    ],
    "similar": [
        "to"
    ],
    "interest": [
        "to",
        "by"
    ],
    "isolate": [
        "from",
        "on",
        "before",
        "down",
        "by"
    ],
    "image": [
        "in",
        "for",
        "by"
    ],
    "trail": [
        "in",
        "to",
        "from",
        "of"
    ],
    "delimit": [
        "to",
        "by",
        "from"
    ],
    "alert": [
        "on",
        "in",
        "for"
    ],
    "header": [
        "with",
        "in",
        "for",
        "to",
        "from"
    ],
    "count": [
        "by",
        "for",
        "with",
        "down",
        "of"
    ],
    "incr": [
        "with"
    ],
    "increment": [
        "off",
        "out"
    ],
    "reference": [
        "in",
        "by",
        "from",
        "after"
    ],
    "vote": [
        "for",
        "on",
        "to",
        "down",
        "up"
    ],
    "pack": [
        "to",
        "by",
        "into",
        "for"
    ],
    "part": [
        "to",
        "of",
        "in",
        "at",
        "with"
    ],
    "explore": [
        "to"
    ],
    "optimise": [
        "for",
        "by",
        "with"
    ],
    "prefix": [
        "by",
        "with",
        "of",
        "for",
        "as"
    ],
    "preserve": [
        "on",
        "upon",
        "to",
        "in",
        "as"
    ],
    "redefine": [
        "by",
        "for"
    ],
    "mirror": [
        "for",
        "of",
        "at",
        "to",
        "as"
    ],
    "signatures": [
        "up",
        "to"
    ],
    "suspend": [
        "by",
        "till",
        "with",
        "on",
        "to"
    ],
    "swipe": [
        "down",
        "up",
        "to",
        "in",
        "on"
    ],
    "cluser": [
        "with"
    ],
    "disappear": [
        "in",
        "after",
        "from"
    ],
    "hierarchy": [
        "to"
    ],
    "inventory": [
        "in",
        "with",
        "to"
    ],
    "pattern": [
        "as",
        "for",
        "from",
        "with"
    ],
    "prop": [
        "to",
        "up",
        "under",
        "in",
        "from"
    ],
    "visible": [
        "in"
    ],
    "occupy": [
        "by"
    ],
    "catalog": [
        "to",
        "up",
        "for"
    ],
    "desire": [
        "without"
    ],
    "separate": [
        "by",
        "from",
        "to"
    ],
    "addcrypted": [
        "to"
    ],
    "remote": [
        "with"
    ],
    "shell": [
        "from"
    ],
    "addelectrocart": [
        "for"
    ],
    "annotate": [
        "with",
        "to",
        "by",
        "for",
        "as"
    ],
    "sanitize": [
        "for",
        "as",
        "between",
        "with",
        "before"
    ],
    "depart": [
        "after",
        "from"
    ],
    "calibrate": [
        "with"
    ],
    "farwarding": [
        "to"
    ],
    "administer": [
        "by"
    ],
    "adorn": [
        "with"
    ],
    "atf": [
        "on"
    ],
    "resource": [
        "with",
        "up"
    ],
    "artifact": [
        "for",
        "from"
    ],
    "establish": [
        "for",
        "without",
        "with",
        "by"
    ],
    "screenshot": [
        "as"
    ],
    "grow": [
        "by",
        "to",
        "until",
        "at",
        "on"
    ],
    "interpret": [
        "as",
        "to",
        "with",
        "through"
    ],
    "violate": [
        "with",
        "before",
        "at",
        "without",
        "in"
    ],
    "flood": [
        "to"
    ],
    "args": [
        "to"
    ],
    "aget": [
        "to"
    ],
    "tunnel": [
        "by",
        "out",
        "down",
        "up"
    ],
    "agree": [
        "to",
        "at",
        "by",
        "of",
        "with"
    ],
    "turn": [
        "off",
        "on",
        "to",
        "into",
        "in"
    ],
    "callback": [
        "with",
        "on"
    ],
    "rewind": [
        "to",
        "for"
    ],
    "alarm": [
        "out",
        "to"
    ],
    "album": [
        "on"
    ],
    "collection": [
        "from",
        "for"
    ],
    "columns": [
        "as"
    ],
    "for": [
        "for",
        "before"
    ],
    "node": [
        "with",
        "down"
    ],
    "space": [
        "before",
        "after",
        "on",
        "between",
        "as"
    ],
    "to": [
        "to"
    ],
    "aliased": [
        "to"
    ],
    "configs": [
        "from",
        "with",
        "by"
    ],
    "permute": [
        "with",
        "for"
    ],
    "alignment": [
        "off",
        "on",
        "to"
    ],
    "deliver": [
        "to",
        "from",
        "until",
        "on"
    ],
    "package": [
        "in",
        "to",
        "from",
        "with",
        "for"
    ],
    "approve": [
        "without",
        "as",
        "by",
        "on"
    ],
    "corrupt": [
        "on",
        "in",
        "for",
        "after"
    ],
    "eliminate": [
        "by",
        "at",
        "with",
        "from",
        "after"
    ],
    "concrete": [
        "for",
        "by",
        "to"
    ],
    "cursor": [
        "with"
    ],
    "cycle": [
        "to",
        "of"
    ],
    "lease": [
        "to"
    ],
    "uri": [
        "for",
        "with",
        "in"
    ],
    "schema": [
        "to",
        "by",
        "with",
        "from",
        "for"
    ],
    "parcel": [
        "from",
        "to"
    ],
    "qualify": [
        "by",
        "for",
        "with",
        "from",
        "as"
    ],
    "slide": [
        "to",
        "up",
        "down",
        "out",
        "by"
    ],
    "reachable": [
        "in",
        "from",
        "through"
    ],
    "halt": [
        "on",
        "with",
        "out",
        "of"
    ],
    "forbid": [
        "for",
        "outside",
        "of",
        "in",
        "on"
    ],
    "explain": [
        "for",
        "with",
        "from",
        "in"
    ],
    "postpone": [
        "up"
    ],
    "path": [
        "to",
        "from",
        "of"
    ],
    "correct": [
        "for",
        "after",
        "in",
        "with",
        "at"
    ],
    "this": [
        "by"
    ],
    "on": [
        "on"
    ],
    "remember": [
        "in",
        "as",
        "for",
        "on",
        "up"
    ],
    "with": [
        "with"
    ],
    "wear": [
        "at",
        "out"
    ],
    "amb": [
        "with"
    ],
    "amend": [
        "to",
        "from"
    ],
    "amount": [
        "to",
        "of",
        "for"
    ],
    "disambiguate": [
        "until"
    ],
    "attack": [
        "with",
        "in",
        "on"
    ],
    "flag": [
        "for"
    ],
    "precede": [
        "by",
        "with",
        "to"
    ],
    "respond": [
        "to",
        "with",
        "as",
        "on",
        "before"
    ],
    "stub": [
        "to",
        "with",
        "on",
        "as",
        "at"
    ],
    "template": [
        "for",
        "with",
        "without"
    ],
    "trash": [
        "as"
    ],
    "anneal": [
        "after"
    ],
    "bed": [
        "from"
    ],
    "differentiate": [
        "between",
        "on"
    ],
    "announce": [
        "for",
        "from",
        "to",
        "with",
        "down"
    ],
    "class": [
        "for",
        "of"
    ],
    "arrive": [
        "on",
        "off"
    ],
    "march": [
        "by"
    ],
    "anticipate": [
        "down",
        "up"
    ],
    "damage": [
        "in",
        "for",
        "by",
        "at",
        "off"
    ],
    "interact": [
        "with",
        "on",
        "to",
        "at",
        "inside"
    ],
    "mouse": [
        "up",
        "down",
        "in",
        "over",
        "on"
    ],
    "aperture": [
        "to"
    ],
    "simulate": [
        "from",
        "out",
        "of",
        "on",
        "for"
    ],
    "discontinue": [
        "after",
        "at",
        "from",
        "before",
        "in"
    ],
    "address": [
        "with",
        "in",
        "to",
        "from",
        "without"
    ],
    "foreground": [
        "at",
        "near"
    ],
    "localize": [
        "for",
        "with"
    ],
    "respect": [
        "for",
        "with"
    ],
    "quiet": [
        "down",
        "with",
        "on",
        "to",
        "for"
    ],
    "redact": [
        "to"
    ],
    "message": [
        "from",
        "to",
        "without",
        "over"
    ],
    "broker": [
        "of",
        "to"
    ],
    "polish": [
        "on"
    ],
    "appoint": [
        "as"
    ],
    "apportion": [
        "by"
    ],
    "approach": [
        "from"
    ],
    "appropriate": [
        "to"
    ],
    "approximate": [
        "by",
        "of",
        "from",
        "to",
        "at"
    ],
    "war": [
        "to"
    ],
    "mute": [
        "for",
        "in"
    ],
    "migrate": [
        "to",
        "from",
        "in",
        "for",
        "with"
    ],
    "bridge": [
        "in",
        "out",
        "to"
    ],
    "threshold": [
        "with"
    ],
    "neighbour": [
        "of",
        "in"
    ],
    "prohibit": [
        "in",
        "from"
    ],
    "ascend": [
        "with",
        "to",
        "after",
        "at"
    ],
    "transmit": [
        "of",
        "in"
    ],
    "sibling": [
        "with",
        "to"
    ],
    "rgba": [
        "for"
    ],
    "moon": [
        "before",
        "near"
    ],
    "negative": [
        "on"
    ],
    "bomb": [
        "out"
    ],
    "arp": [
        "to"
    ],
    "cat": [
        "to"
    ],
    "spread": [
        "to",
        "from",
        "out",
        "into",
        "of"
    ],
    "deregister": [
        "from"
    ],
    "omit": [
        "from",
        "for",
        "on"
    ],
    "artwork": [
        "to"
    ],
    "mutate": [
        "by",
        "to",
        "with",
        "in",
        "at"
    ],
    "polygon": [
        "with",
        "to"
    ],
    "substitute": [
        "for",
        "with",
        "in",
        "to",
        "into"
    ],
    "unbox": [
        "as",
        "by",
        "to"
    ],
    "bcd": [
        "to",
        "with"
    ],
    "descend": [
        "from",
        "for",
        "with",
        "into",
        "on"
    ],
    "ascii": [
        "to",
        "from"
    ],
    "aspect": [
        "on",
        "with"
    ],
    "correspond": [
        "in",
        "to"
    ],
    "whitespace": [
        "in"
    ],
    "jenkins": [
        "in"
    ],
    "offload": [
        "in"
    ],
    "normalise": [
        "to"
    ],
    "instrument": [
        "with",
        "for"
    ],
    "subset": [
        "from",
        "of",
        "for",
        "around",
        "by"
    ],
    "permit": [
        "to",
        "by",
        "on",
        "of",
        "in"
    ],
    "tolerate": [
        "with"
    ],
    "msg": [
        "by",
        "to",
        "from",
        "in",
        "off"
    ],
    "stale": [
        "after"
    ],
    "intend": [
        "to"
    ],
    "augment": [
        "with",
        "to",
        "from",
        "by"
    ],
    "designate": [
        "by",
        "for"
    ],
    "reassign": [
        "to",
        "for"
    ],
    "assume": [
        "with",
        "to",
        "in",
        "by",
        "before"
    ],
    "uncompress": [
        "to",
        "into",
        "out"
    ],
    "assure": [
        "to",
        "without",
        "with"
    ],
    "recompute": [
        "after",
        "down",
        "out",
        "up",
        "by"
    ],
    "renew": [
        "with",
        "to",
        "of",
        "on",
        "after"
    ],
    "seal": [
        "with"
    ],
    "bootstrap": [
        "with",
        "from",
        "to",
        "up"
    ],
    "stick": [
        "in",
        "to",
        "around",
        "after",
        "at"
    ],
    "hit": [
        "by",
        "to",
        "in",
        "for",
        "against"
    ],
    "extrude": [
        "as"
    ],
    "ring": [
        "out",
        "in",
        "with"
    ],
    "eat": [
        "until",
        "to",
        "before",
        "from",
        "as"
    ],
    "party": [
        "of",
        "with"
    ],
    "stamp": [
        "with"
    ],
    "plot": [
        "at",
        "to",
        "for"
    ],
    "attend": [
        "by"
    ],
    "in": [
        "in"
    ],
    "want": [
        "to",
        "on",
        "with"
    ],
    "audit": [
        "as",
        "in",
        "on",
        "to",
        "out"
    ],
    "issue": [
        "at",
        "on",
        "to",
        "for",
        "down"
    ],
    "scheme": [
        "to"
    ],
    "author": [
        "on",
        "in",
        "for"
    ],
    "maintain": [
        "on",
        "as",
        "by",
        "in",
        "after"
    ],
    "swallow": [
        "from",
        "through",
        "to",
        "until",
        "up"
    ],
    "badge": [
        "for",
        "with"
    ],
    "decay": [
        "at"
    ],
    "decide": [
        "on",
        "for",
        "to",
        "by",
        "with"
    ],
    "guess": [
        "from",
        "up",
        "by",
        "for",
        "at"
    ],
    "provision": [
        "in",
        "with",
        "at"
    ],
    "refine": [
        "to",
        "with",
        "by",
        "for"
    ],
    "wire": [
        "up",
        "into",
        "to",
        "with"
    ],
    "autocommit": [
        "off"
    ],
    "cannot": [
        "with"
    ],
    "automate": [
        "by"
    ],
    "autoregister": [
        "to"
    ],
    "autosave": [
        "to"
    ],
    "zone": [
        "with",
        "to"
    ],
    "average": [
        "out",
        "with"
    ],
    "avoid": [
        "on",
        "in",
        "for",
        "by",
        "off"
    ],
    "awake": [
        "from"
    ],
    "awaken": [
        "from"
    ],
    "award": [
        "for",
        "on"
    ],
    "azure": [
        "up"
    ],
    "inv": [
        "to",
        "for",
        "from"
    ],
    "vec": [
        "to",
        "from"
    ],
    "burst": [
        "into"
    ],
    "bill": [
        "to"
    ],
    "backpressure": [
        "off"
    ],
    "action": [
        "with",
        "from"
    ],
    "config": [
        "for",
        "in"
    ],
    "data": [
        "out",
        "from",
        "to"
    ],
    "method": [
        "with",
        "for",
        "on"
    ],
    "random": [
        "between",
        "in",
        "to"
    ],
    "url": [
        "with",
        "on"
    ],
    "bail": [
        "out"
    ],
    "ban": [
        "for",
        "from"
    ],
    "hover": [
        "over",
        "on",
        "off"
    ],
    "barge": [
        "in"
    ],
    "bark": [
        "to"
    ],
    "bas58": [
        "to",
        "with"
    ],
    "slave": [
        "of",
        "with",
        "up"
    ],
    "bash": [
        "to"
    ],
    "diagram": [
        "to",
        "in"
    ],
    "std": [
        "out"
    ],
    "bat": [
        "up"
    ],
    "bch": [
        "to"
    ],
    "sell": [
        "at",
        "as"
    ],
    "overload": [
        "with",
        "as",
        "on",
        "of"
    ],
    "bear": [
        "to",
        "in"
    ],
    "become": [
        "from",
        "by",
        "for",
        "after",
        "at"
    ],
    "come": [
        "before",
        "from",
        "of",
        "after",
        "down"
    ],
    "redeploy": [
        "with",
        "to"
    ],
    "exclusive": [
        "to"
    ],
    "behave": [
        "as",
        "like"
    ],
    "bench": [
        "in",
        "of"
    ],
    "specialize": [
        "for"
    ],
    "bestow": [
        "for",
        "to",
        "with"
    ],
    "bet": [
        "in"
    ],
    "beware": [
        "of",
        "after"
    ],
    "wind": [
        "up",
        "down",
        "to",
        "from",
        "with"
    ],
    "bib": [
        "to"
    ],
    "bid": [
        "with",
        "on"
    ],
    "relay": [
        "with",
        "to",
        "without",
        "from"
    ],
    "decimal": [
        "from",
        "for"
    ],
    "rectangle": [
        "for",
        "by",
        "in",
        "on",
        "to"
    ],
    "biimp": [
        "with"
    ],
    "binarize": [
        "on"
    ],
    "floor": [
        "as",
        "to",
        "of",
        "in"
    ],
    "reposition": [
        "after",
        "on"
    ],
    "birth": [
        "by"
    ],
    "shave": [
        "off"
    ],
    "bite": [
        "on",
        "off",
        "at"
    ],
    "bitset": [
        "from",
        "to"
    ],
    "blacklist": [
        "in",
        "from",
        "after",
        "to",
        "with"
    ],
    "sheet": [
        "with"
    ],
    "blast": [
        "for"
    ],
    "blaze": [
        "down",
        "on",
        "up"
    ],
    "blog": [
        "to"
    ],
    "blow": [
        "up",
        "to",
        "on"
    ],
    "grey": [
        "out"
    ],
    "blur": [
        "at",
        "with"
    ],
    "bnd": [
        "up",
        "down"
    ],
    "board": [
        "to",
        "with"
    ],
    "bookkeeping": [
        "for"
    ],
    "borrow": [
        "from"
    ],
    "unbounded": [
        "as"
    ],
    "brace": [
        "around"
    ],
    "nullify": [
        "for",
        "to",
        "at"
    ],
    "chop": [
        "off",
        "at",
        "around"
    ],
    "branch": [
        "from"
    ],
    "breakpoint": [
        "of",
        "on"
    ],
    "watchpoint": [
        "out",
        "of"
    ],
    "breakpoints": [
        "from"
    ],
    "breed": [
        "with"
    ],
    "bridger": [
        "to"
    ],
    "remain": [
        "to",
        "on",
        "up",
        "as",
        "in"
    ],
    "bt": [
        "to",
        "for"
    ],
    "bubble": [
        "up",
        "down",
        "on",
        "to",
        "out"
    ],
    "buff": [
        "to"
    ],
    "ride": [
        "for",
        "in"
    ],
    "organize": [
        "in",
        "by",
        "up"
    ],
    "tool": [
        "to",
        "from",
        "for"
    ],
    "style": [
        "by",
        "to",
        "for"
    ],
    "unregistered": [
        "on"
    ],
    "buildv4binding": [
        "from"
    ],
    "buildv6binding": [
        "from"
    ],
    "tue": [
        "to"
    ],
    "busy": [
        "for",
        "since",
        "out"
    ],
    "without": [
        "without"
    ],
    "button": [
        "down",
        "out",
        "up"
    ],
    "snap": [
        "to",
        "with",
        "without",
        "after",
        "from"
    ],
    "buy": [
        "in",
        "at",
        "with"
    ],
    "byte315": [
        "to"
    ],
    "pdu": [
        "to"
    ],
    "rebind": [
        "as",
        "to"
    ],
    "cable": [
        "to"
    ],
    "dereference": [
        "in",
        "for",
        "to",
        "of"
    ],
    "caculate": [
        "in"
    ],
    "observe": [
        "on",
        "in",
        "of",
        "with",
        "to"
    ],
    "price": [
        "from",
        "with",
        "to"
    ],
    "plant": [
        "from",
        "to",
        "at"
    ],
    "rot": [
        "with"
    ],
    "div": [
        "up"
    ],
    "slope": [
        "to"
    ],
    "race": [
        "in",
        "to"
    ],
    "rain": [
        "at",
        "in"
    ],
    "corner": [
        "of",
        "to"
    ],
    "mass": [
        "with",
        "for",
        "by",
        "from"
    ],
    "fair": [
        "with"
    ],
    "transition": [
        "to",
        "between",
        "from"
    ],
    "replicas": [
        "up",
        "to"
    ],
    "charge": [
        "from",
        "through"
    ],
    "mysql": [
        "to",
        "after"
    ],
    "calendar": [
        "with"
    ],
    "market": [
        "for",
        "in"
    ],
    "reactivate": [
        "with"
    ],
    "scream": [
        "to"
    ],
    "hypen": [
        "to"
    ],
    "camelhump": [
        "to"
    ],
    "camelize": [
        "in"
    ],
    "live": [
        "in",
        "out",
        "at",
        "on",
        "to"
    ],
    "camunda": [
        "out"
    ],
    "paginate": [
        "by",
        "with"
    ],
    "cool": [
        "down",
        "to",
        "from",
        "with"
    ],
    "craft": [
        "in"
    ],
    "discharge": [
        "as"
    ],
    "harvest": [
        "from",
        "with",
        "by",
        "down",
        "up"
    ],
    "hear": [
        "about",
        "from"
    ],
    "practice": [
        "by"
    ],
    "preempt": [
        "from",
        "for",
        "on"
    ],
    "preview": [
        "with",
        "to",
        "in",
        "from",
        "down"
    ],
    "refer": [
        "to",
        "by",
        "in",
        "out",
        "of"
    ],
    "steer": [
        "to",
        "with"
    ],
    "subsume": [
        "by"
    ],
    "teach": [
        "by"
    ],
    "burrow": [
        "in"
    ],
    "commence": [
        "up"
    ],
    "pipe": [
        "to",
        "on",
        "after",
        "as"
    ],
    "disassemble": [
        "to"
    ],
    "dock": [
        "to",
        "with"
    ],
    "drill": [
        "down",
        "through",
        "up",
        "to"
    ],
    "dye": [
        "of"
    ],
    "elevate": [
        "to"
    ],
    "emulate": [
        "for",
        "on",
        "down",
        "of"
    ],
    "entitle": [
        "by",
        "in"
    ],
    "equip": [
        "with",
        "to"
    ],
    "represent": [
        "as",
        "by",
        "of",
        "in"
    ],
    "expose": [
        "as",
        "to",
        "for",
        "by",
        "in"
    ],
    "expunge": [
        "by",
        "in"
    ],
    "fling": [
        "to",
        "down"
    ],
    "fly": [
        "to"
    ],
    "forge": [
        "for"
    ],
    "fork": [
        "from",
        "with",
        "to"
    ],
    "getter": [
        "with",
        "without",
        "to",
        "for",
        "into"
    ],
    "glide": [
        "with"
    ],
    "hack": [
        "off",
        "for",
        "around",
        "on"
    ],
    "hire": [
        "from"
    ],
    "inline": [
        "to",
        "into",
        "in"
    ],
    "inspect": [
        "in",
        "by",
        "with",
        "from",
        "without"
    ],
    "jump": [
        "to",
        "out",
        "of",
        "off",
        "for"
    ],
    "lift": [
        "from",
        "for",
        "off",
        "with",
        "after"
    ],
    "manipulate": [
        "with",
        "like",
        "from",
        "to"
    ],
    "mate": [
        "with"
    ],
    "morph": [
        "for",
        "to",
        "from",
        "into"
    ],
    "originate": [
        "to",
        "from"
    ],
    "parallelize": [
        "on"
    ],
    "proceed": [
        "to",
        "after",
        "with",
        "without",
        "at"
    ],
    "progress": [
        "on",
        "since"
    ],
    "snow": [
        "at",
        "in"
    ],
    "reclaim": [
        "for"
    ],
    "rerun": [
        "after"
    ],
    "resort": [
        "to"
    ],
    "folder": [
        "by",
        "from",
        "with"
    ],
    "revise": [
        "with"
    ],
    "scrub": [
        "by",
        "in",
        "with"
    ],
    "shorten": [
        "to",
        "with"
    ],
    "spend": [
        "by",
        "in",
        "since"
    ],
    "stay": [
        "in",
        "out",
        "after",
        "behind",
        "on"
    ],
    "syphon": [
        "from"
    ],
    "teleport": [
        "to",
        "on",
        "in",
        "down",
        "with"
    ],
    "transport": [
        "of",
        "to",
        "for",
        "in",
        "down"
    ],
    "travel": [
        "to",
        "from",
        "for",
        "on"
    ],
    "unify": [
        "in"
    ],
    "participate": [
        "in"
    ],
    "canopy": [
        "to"
    ],
    "cant": [
        "without",
        "to",
        "with",
        "on",
        "for"
    ],
    "canvas": [
        "to"
    ],
    "carve": [
        "to",
        "out"
    ],
    "co": [
        "to",
        "as",
        "from"
    ],
    "colour": [
        "for"
    ],
    "circuit": [
        "with",
        "in"
    ],
    "draught": [
        "out"
    ],
    "pile": [
        "up",
        "without",
        "for",
        "to",
        "in"
    ],
    "ramp": [
        "up",
        "to"
    ],
    "fragment": [
        "to"
    ],
    "catchable": [
        "as",
        "of"
    ],
    "categorize": [
        "in",
        "by"
    ],
    "fish": [
        "for"
    ],
    "reboot": [
        "with",
        "to",
        "in"
    ],
    "spiral": [
        "with"
    ],
    "cdf": [
        "up"
    ],
    "centre": [
        "on",
        "of"
    ],
    "reg": [
        "off",
        "on"
    ],
    "idx": [
        "in"
    ],
    "cow": [
        "on"
    ],
    "supply": [
        "for",
        "up",
        "by",
        "with"
    ],
    "changelog": [
        "on"
    ],
    "static": [
        "with"
    ],
    "pdf": [
        "to"
    ],
    "disagree": [
        "with"
    ],
    "nudge": [
        "down",
        "for",
        "up"
    ],
    "rethrow": [
        "as",
        "on",
        "from"
    ],
    "hitted": [
        "on"
    ],
    "spring": [
        "after",
        "before",
        "with",
        "over"
    ],
    "react": [
        "to",
        "on"
    ],
    "reify": [
        "with",
        "by"
    ],
    "deserialized": [
        "as"
    ],
    "obscure": [
        "by"
    ],
    "exempt": [
        "by",
        "from"
    ],
    "raid": [
        "by"
    ],
    "uid": [
        "to"
    ],
    "recursive": [
        "on",
        "to",
        "with",
        "in"
    ],
    "max": [
        "up",
        "out",
        "with"
    ],
    "status": [
        "on",
        "off"
    ],
    "uncheck": [
        "to"
    ],
    "rectify": [
        "with",
        "on",
        "to"
    ],
    "regress": [
        "to",
        "out"
    ],
    "gps": [
        "to"
    ],
    "chew": [
        "up"
    ],
    "chomp": [
        "to"
    ],
    "chord": [
        "on",
        "as"
    ],
    "warm": [
        "up"
    ],
    "absolute": [
        "with"
    ],
    "convolve": [
        "with"
    ],
    "smooth": [
        "to",
        "by",
        "on",
        "out",
        "of"
    ],
    "ds": [
        "for",
        "from",
        "to",
        "with",
        "by"
    ],
    "clang": [
        "as",
        "from",
        "of",
        "in",
        "for"
    ],
    "clash": [
        "of"
    ],
    "regex": [
        "like"
    ],
    "script": [
        "from",
        "in"
    ],
    "whitelisted": [
        "without",
        "in"
    ],
    "cleanse": [
        "of"
    ],
    "employ": [
        "by"
    ],
    "leash": [
        "to"
    ],
    "refund": [
        "to"
    ],
    "splitted": [
        "of"
    ],
    "pre": [
        "on",
        "out",
        "in",
        "as",
        "for"
    ],
    "libraries": [
        "to"
    ],
    "tend": [
        "to"
    ],
    "clob": [
        "before",
        "after",
        "to"
    ],
    "enrich": [
        "with",
        "by",
        "before"
    ],
    "speaker": [
        "on"
    ],
    "odd": [
        "to"
    ],
    "side": [
        "of"
    ],
    "clue": [
        "to"
    ],
    "salt": [
        "into"
    ],
    "coalesce": [
        "to",
        "with",
        "down"
    ],
    "primitives": [
        "to"
    ],
    "cogroup": [
        "to",
        "out"
    ],
    "coin": [
        "to",
        "with",
        "for"
    ],
    "collate": [
        "for",
        "on"
    ],
    "parameter": [
        "from",
        "as",
        "of",
        "with"
    ],
    "above": [
        "above"
    ],
    "colorize": [
        "by"
    ],
    "vector": [
        "of",
        "to"
    ],
    "comb": [
        "for"
    ],
    "exert": [
        "during",
        "with"
    ],
    "commensurate": [
        "with"
    ],
    "veto": [
        "from",
        "for"
    ],
    "stag": [
        "for"
    ],
    "skylark": [
        "to",
        "in"
    ],
    "communicate": [
        "to"
    ],
    "numeric": [
        "at"
    ],
    "complain": [
        "for",
        "about",
        "under",
        "in"
    ],
    "comply": [
        "with",
        "to"
    ],
    "component": [
        "with",
        "of",
        "inside"
    ],
    "recognise": [
        "as",
        "with",
        "of"
    ],
    "generalize": [
        "with",
        "to"
    ],
    "orphan": [
        "as"
    ],
    "port": [
        "for",
        "to",
        "down",
        "up",
        "as"
    ],
    "conjunct": [
        "with"
    ],
    "enterprise": [
        "with"
    ],
    "wifi": [
        "with",
        "to"
    ],
    "refuse": [
        "with",
        "for",
        "on"
    ],
    "wildcard": [
        "from"
    ],
    "consist": [
        "of",
        "from"
    ],
    "consolidate": [
        "with",
        "for"
    ],
    "constitute": [
        "from"
    ],
    "exsting": [
        "on",
        "with"
    ],
    "elaborate": [
        "to"
    ],
    "feed": [
        "before",
        "at"
    ],
    "digits": [
        "to"
    ],
    "content": [
        "as",
        "of",
        "to",
        "by",
        "since"
    ],
    "contribute": [
        "to",
        "up",
        "from"
    ],
    "spatial": [
        "for"
    ],
    "translucent": [
        "after",
        "before"
    ],
    "tint": [
        "to"
    ],
    "foot": [
        "to",
        "from"
    ],
    "rail": [
        "to",
        "from"
    ],
    "reinforce": [
        "to",
        "from"
    ],
    "shade": [
        "down",
        "to",
        "from",
        "without"
    ],
    "matrix": [
        "for"
    ],
    "ln": [
        "to",
        "from"
    ],
    "tlphd": [
        "to"
    ],
    "transformer": [
        "to",
        "from",
        "with"
    ],
    "analog": [
        "in",
        "to",
        "from"
    ],
    "randomize": [
        "for"
    ],
    "convertgray": [
        "to"
    ],
    "doc": [
        "to",
        "with"
    ],
    "dir": [
        "at"
    ],
    "wrapper": [
        "to"
    ],
    "realm": [
        "of",
        "out",
        "for",
        "in",
        "to"
    ],
    "rel": [
        "to",
        "with"
    ],
    "couch": [
        "during",
        "on"
    ],
    "weave": [
        "after",
        "at",
        "around",
        "on",
        "for"
    ],
    "finger": [
        "down",
        "to"
    ],
    "misfire": [
        "in"
    ],
    "nulls": [
        "out",
        "in"
    ],
    "weekend": [
        "of"
    ],
    "metric": [
        "of"
    ],
    "countfind": [
        "by",
        "for",
        "on",
        "of",
        "to"
    ],
    "course": [
        "into"
    ],
    "rat": [
        "as",
        "to",
        "for",
        "from",
        "up"
    ],
    "relativize": [
        "by",
        "from",
        "to",
        "of"
    ],
    "resend": [
        "after"
    ],
    "materialize": [
        "to",
        "in",
        "up",
        "on"
    ],
    "escalate": [
        "to",
        "on",
        "up"
    ],
    "tfc": [
        "from"
    ],
    "fc": [
        "to",
        "from"
    ],
    "undock": [
        "without",
        "with"
    ],
    "unknown": [
        "out",
        "on"
    ],
    "cruise": [
        "with"
    ],
    "crumble": [
        "below",
        "in"
    ],
    "demand": [
        "from"
    ],
    "ctid": [
        "to"
    ],
    "ctrl": [
        "down"
    ],
    "memcpy": [
        "to"
    ],
    "cumulate": [
        "in"
    ],
    "cup": [
        "to"
    ],
    "curl": [
        "up"
    ],
    "honour": [
        "on"
    ],
    "perm": [
        "for"
    ],
    "csr": [
        "by"
    ],
    "xcoo": [
        "to"
    ],
    "custom": [
        "off",
        "with",
        "out",
        "from"
    ],
    "dilate": [
        "from"
    ],
    "cv": [
        "to"
    ],
    "poly": [
        "to",
        "at"
    ],
    "seq": [
        "to",
        "from",
        "with"
    ],
    "pyr": [
        "up",
        "down"
    ],
    "cvar": [
        "without"
    ],
    "cvtsd": [
        "to"
    ],
    "sd": [
        "with",
        "from"
    ],
    "cvtss": [
        "to",
        "off"
    ],
    "after": [
        "after"
    ],
    "damp": [
        "over"
    ],
    "darken": [
        "by"
    ],
    "station": [
        "of"
    ],
    "packet": [
        "out"
    ],
    "holiday": [
        "with"
    ],
    "relocate": [
        "to",
        "in"
    ],
    "databinding": [
        "to"
    ],
    "datanode": [
        "down",
        "up"
    ],
    "dataset": [
        "to",
        "at",
        "from",
        "with"
    ],
    "timestamp": [
        "from"
    ],
    "diff": [
        "with",
        "down",
        "up"
    ],
    "setter": [
        "for"
    ],
    "parameterize": [
        "with"
    ],
    "tenant": [
        "in",
        "to",
        "like"
    ],
    "deattach": [
        "from"
    ],
    "localise": [
        "with"
    ],
    "gauge": [
        "to"
    ],
    "decapitalize": [
        "like"
    ],
    "panel": [
        "as",
        "by"
    ],
    "decimate": [
        "on"
    ],
    "decipher": [
        "with"
    ],
    "decoder": [
        "for"
    ],
    "decommission": [
        "of",
        "to"
    ],
    "deconstruct": [
        "to",
        "of"
    ],
    "decr": [
        "with"
    ],
    "deduce": [
        "for",
        "of",
        "from"
    ],
    "deduct": [
        "at",
        "to"
    ],
    "children": [
        "for"
    ],
    "same": [
        "as"
    ],
    "deform": [
        "for"
    ],
    "degenerate": [
        "to"
    ],
    "rasterize": [
        "to"
    ],
    "minutes": [
        "to"
    ],
    "deidentify": [
        "from"
    ],
    "propose": [
        "for"
    ],
    "surround": [
        "with",
        "by",
        "in"
    ],
    "delist": [
        "from"
    ],
    "sulphur": [
        "on"
    ],
    "dereferenced": [
        "for"
    ],
    "desc": [
        "to",
        "by"
    ],
    "deselect": [
        "by"
    ],
    "replay": [
        "on",
        "in",
        "to",
        "over",
        "under"
    ],
    "deserializes": [
        "with"
    ],
    "design": [
        "with",
        "to"
    ],
    "destine": [
        "to"
    ],
    "scope": [
        "out",
        "of",
        "down",
        "up"
    ],
    "scrap": [
        "at"
    ],
    "diagnose": [
        "down"
    ],
    "dialect": [
        "in"
    ],
    "differ": [
        "from",
        "at",
        "by"
    ],
    "dig": [
        "with",
        "in",
        "up"
    ],
    "slash": [
        "to",
        "with"
    ],
    "dijkstra": [
        "to"
    ],
    "dip": [
        "to"
    ],
    "meta": [
        "down",
        "to",
        "on"
    ],
    "dominate": [
        "by",
        "to"
    ],
    "disassociate": [
        "from",
        "with",
        "in",
        "of"
    ],
    "disco": [
        "up"
    ],
    "discount": [
        "with"
    ],
    "intimate": [
        "for"
    ],
    "disguise": [
        "to"
    ],
    "displace": [
        "by"
    ],
    "dissociate": [
        "from"
    ],
    "triangle": [
        "down",
        "up"
    ],
    "distort": [
        "to"
    ],
    "divert": [
        "to",
        "before",
        "up",
        "from"
    ],
    "duplex": [
        "with"
    ],
    "inverse": [
        "to"
    ],
    "scoped": [
        "for",
        "to",
        "outside",
        "into"
    ],
    "refactor": [
        "to"
    ],
    "unzip": [
        "to",
        "in",
        "from",
        "with",
        "as"
    ],
    "soap": [
        "to",
        "as"
    ],
    "dodge": [
        "in"
    ],
    "spark": [
        "with",
        "out"
    ],
    "experience": [
        "at",
        "since",
        "between",
        "to"
    ],
    "dogenerate": [
        "to"
    ],
    "downgrade": [
        "to",
        "for"
    ],
    "drug": [
        "to"
    ],
    "dsl": [
        "with"
    ],
    "dt14": [
        "to"
    ],
    "dulicate": [
        "to"
    ],
    "stitch": [
        "to"
    ],
    "attr": [
        "to"
    ],
    "item": [
        "with"
    ],
    "let": [
        "below",
        "in",
        "up"
    ],
    "earth": [
        "to"
    ],
    "ecl": [
        "to"
    ],
    "equ": [
        "to"
    ],
    "induce": [
        "up",
        "for",
        "from"
    ],
    "symmetric": [
        "with"
    ],
    "ele": [
        "to"
    ],
    "elect": [
        "on",
        "for"
    ],
    "element": [
        "with",
        "of",
        "on"
    ],
    "workspace": [
        "for",
        "from"
    ],
    "elementwise": [
        "in"
    ],
    "ellipse": [
        "to"
    ],
    "emu": [
        "to"
    ],
    "proj": [
        "to",
        "under",
        "for"
    ],
    "screw": [
        "up"
    ],
    "encapsulate": [
        "in"
    ],
    "encodeable": [
        "to"
    ],
    "engage": [
        "in"
    ],
    "enlarge": [
        "for",
        "to",
        "by"
    ],
    "enlist": [
        "in",
        "for"
    ],
    "enroll": [
        "in"
    ],
    "recommend": [
        "for",
        "to",
        "with",
        "in",
        "from"
    ],
    "shoot": [
        "from",
        "with"
    ],
    "wo": [
        "with"
    ],
    "unmarked": [
        "as"
    ],
    "utils": [
        "to"
    ],
    "entropy": [
        "over"
    ],
    "ingest": [
        "with",
        "from",
        "until"
    ],
    "anded": [
        "with"
    ],
    "txt": [
        "to"
    ],
    "envelope": [
        "to",
        "from"
    ],
    "epoll": [
        "out"
    ],
    "equalize": [
        "with",
        "in"
    ],
    "error": [
        "out",
        "on"
    ],
    "hydrate": [
        "from",
        "of"
    ],
    "evade": [
        "on",
        "off"
    ],
    "unroll": [
        "from"
    ],
    "reprocess": [
        "for"
    ],
    "evidence": [
        "to"
    ],
    "excel": [
        "after",
        "before",
        "from",
        "to",
        "for"
    ],
    "examine": [
        "as",
        "to",
        "around",
        "for"
    ],
    "latch": [
        "on",
        "to",
        "for"
    ],
    "snoop": [
        "on",
        "by"
    ],
    "exercise": [
        "in",
        "with"
    ],
    "exhaust": [
        "from",
        "with"
    ],
    "tokenize": [
        "to",
        "with",
        "for",
        "by",
        "as"
    ],
    "unsorted": [
        "with"
    ],
    "experiment": [
        "to"
    ],
    "explicit": [
        "off"
    ],
    "express": [
        "by",
        "as"
    ],
    "ext": [
        "for"
    ],
    "params": [
        "with"
    ],
    "question": [
        "from"
    ],
    "op": [
        "with"
    ],
    "biome": [
        "by"
    ],
    "ps": [
        "to"
    ],
    "libs": [
        "for"
    ],
    "supervise": [
        "by"
    ],
    "extractor": [
        "with"
    ],
    "fabricate": [
        "from"
    ],
    "callget": [
        "after",
        "on",
        "with"
    ],
    "if": [
        "before"
    ],
    "fattr": [
        "to"
    ],
    "favor": [
        "over",
        "at",
        "in"
    ],
    "featurize": [
        "to"
    ],
    "federate": [
        "with"
    ],
    "resign": [
        "with",
        "from",
        "before"
    ],
    "ff": [
        "to"
    ],
    "fiddle": [
        "with"
    ],
    "figure": [
        "out",
        "to",
        "up",
        "from"
    ],
    "templates": [
        "by",
        "without",
        "with"
    ],
    "filesize": [
        "to"
    ],
    "prepends": [
        "to"
    ],
    "fin": [
        "by"
    ],
    "prefetch": [
        "for"
    ],
    "instruct": [
        "to"
    ],
    "lambda": [
        "with",
        "in",
        "for"
    ],
    "partial": [
        "on"
    ],
    "unassigned": [
        "from",
        "as",
        "to"
    ],
    "inside": [
        "inside"
    ],
    "outside": [
        "outside"
    ],
    "stall": [
        "up",
        "on",
        "till",
        "in",
        "down"
    ],
    "between": [
        "between"
    ],
    "constructor": [
        "with"
    ],
    "heartbeat": [
        "to"
    ],
    "instruction": [
        "before"
    ],
    "notice": [
        "from",
        "in"
    ],
    "of": [
        "of"
    ],
    "out": [
        "out"
    ],
    "registry": [
        "of"
    ],
    "x": [
        "for",
        "to"
    ],
    "flee": [
        "on",
        "off"
    ],
    "flipbook": [
        "at"
    ],
    "flock": [
        "off",
        "on",
        "to"
    ],
    "checksum": [
        "out"
    ],
    "flutter": [
        "for"
    ],
    "fomate": [
        "to"
    ],
    "foo": [
        "with",
        "to"
    ],
    "fracture": [
        "from"
    ],
    "pitch": [
        "up"
    ],
    "info": [
        "out",
        "with"
    ],
    "slot": [
        "with",
        "to",
        "as",
        "from",
        "of"
    ],
    "projective": [
        "to"
    ],
    "funits": [
        "to"
    ],
    "further": [
        "up",
        "from",
        "of"
    ],
    "leverage": [
        "to",
        "for",
        "of"
    ],
    "fuzz": [
        "down",
        "up"
    ],
    "gal": [
        "to"
    ],
    "gallon": [
        "to"
    ],
    "garble": [
        "by"
    ],
    "gather": [
        "for",
        "from",
        "with",
        "to",
        "in"
    ],
    "gear": [
        "down"
    ],
    "unwind": [
        "from",
        "for"
    ],
    "accord": [
        "to"
    ],
    "geodist": [
        "with"
    ],
    "geom": [
        "from"
    ],
    "synchronise": [
        "with"
    ],
    "involve": [
        "in"
    ],
    "hdfs": [
        "down",
        "after"
    ],
    "destructuring": [
        "out",
        "of",
        "in"
    ],
    "grid": [
        "in",
        "by",
        "with",
        "before",
        "inside"
    ],
    "backlight": [
        "off",
        "during"
    ],
    "supplement": [
        "with",
        "into",
        "from"
    ],
    "rely": [
        "on"
    ],
    "quantize": [
        "from",
        "to"
    ],
    "cond": [
        "out",
        "down",
        "to"
    ],
    "dont": [
        "with"
    ],
    "discuss": [
        "without",
        "on",
        "with"
    ],
    "distinguish": [
        "with"
    ],
    "vert": [
        "with",
        "in"
    ],
    "at": [
        "at"
    ],
    "freestanding": [
        "for"
    ],
    "guarantee": [
        "in"
    ],
    "hive": [
        "with",
        "from",
        "to",
        "for"
    ],
    "help": [
        "with",
        "out",
        "to"
    ],
    "dnon": [
        "to",
        "as"
    ],
    "properties": [
        "as"
    ],
    "rack": [
        "to",
        "for"
    ],
    "lay": [
        "out",
        "in"
    ],
    "loan": [
        "with",
        "of",
        "to"
    ],
    "tune": [
        "to",
        "for",
        "out"
    ],
    "steal": [
        "at",
        "from"
    ],
    "memorize": [
        "to"
    ],
    "mess": [
        "up",
        "with"
    ],
    "rw": [
        "for",
        "up"
    ],
    "c": [
        "after"
    ],
    "non": [
        "with",
        "in"
    ],
    "gzipped": [
        "with"
    ],
    "incrementing": [
        "by"
    ],
    "oversubscribed": [
        "by"
    ],
    "struct": [
        "in",
        "to"
    ],
    "pred": [
        "from"
    ],
    "neigh": [
        "of"
    ],
    "quarantine": [
        "by"
    ],
    "ram": [
        "for",
        "in"
    ],
    "remind": [
        "to"
    ],
    "egistered": [
        "of"
    ],
    "lag": [
        "from",
        "in"
    ],
    "ssp": [
        "with",
        "from"
    ],
    "applicable": [
        "in"
    ],
    "smash": [
        "into"
    ],
    "snmp": [
        "out"
    ],
    "stock": [
        "out"
    ],
    "refurbish": [
        "on",
        "in"
    ],
    "traning": [
        "by"
    ],
    "unconnected": [
        "out"
    ],
    "period": [
        "from",
        "to"
    ],
    "seperated": [
        "by",
        "with",
        "in"
    ],
    "vary": [
        "by",
        "on"
    ],
    "webhook": [
        "for"
    ],
    "workflow": [
        "by",
        "to"
    ],
    "getpop": [
        "up"
    ],
    "getstate": [
        "from"
    ],
    "incorrect": [
        "of",
        "with"
    ],
    "paritioning": [
        "into"
    ],
    "gossip": [
        "to"
    ],
    "grammar": [
        "from"
    ],
    "greet": [
        "by"
    ],
    "groom": [
        "by"
    ],
    "growl": [
        "out"
    ],
    "gzip": [
        "with"
    ],
    "hammer": [
        "on"
    ],
    "sniff": [
        "on"
    ],
    "bluetooth": [
        "to"
    ],
    "rancid": [
        "down"
    ],
    "unset": [
        "off"
    ],
    "boil": [
        "in"
    ],
    "windowing": [
        "to"
    ],
    "reindexing": [
        "upon"
    ],
    "snooze": [
        "until"
    ],
    "hav": [
        "from"
    ],
    "heapify": [
        "down",
        "up"
    ],
    "hebrew": [
        "with"
    ],
    "sigma": [
        "for"
    ],
    "quiesce": [
        "by",
        "for",
        "with"
    ],
    "base58": [
        "with"
    ],
    "hijri": [
        "with"
    ],
    "hollow": [
        "out",
        "from"
    ],
    "homogenise": [
        "from"
    ],
    "vanish": [
        "with"
    ],
    "hump": [
        "to"
    ],
    "hunt": [
        "for"
    ],
    "hyperlink": [
        "to"
    ],
    "hyphen": [
        "in"
    ],
    "ice": [
        "from"
    ],
    "idf": [
        "from"
    ],
    "iframe": [
        "with",
        "on"
    ],
    "imp": [
        "with"
    ],
    "impose": [
        "on"
    ],
    "sortby": [
        "in"
    ],
    "evals": [
        "out"
    ],
    "ind": [
        "to"
    ],
    "indicate": [
        "of",
        "to",
        "by"
    ],
    "loop": [
        "until",
        "for",
        "at",
        "over",
        "through"
    ],
    "inizialize": [
        "from"
    ],
    "inquire": [
        "with"
    ],
    "weigh": [
        "in"
    ],
    "python": [
        "as"
    ],
    "mode": [
        "by"
    ],
    "uninstall": [
        "without",
        "from"
    ],
    "intermediate": [
        "for",
        "to"
    ],
    "sip": [
        "to"
    ],
    "internet": [
        "up"
    ],
    "interpose": [
        "on",
        "by",
        "off"
    ],
    "reap": [
        "up"
    ],
    "intialize": [
        "with"
    ],
    "invimp": [
        "with"
    ],
    "ips": [
        "to"
    ],
    "land": [
        "out"
    ],
    "unplug": [
        "from"
    ],
    "manufacture": [
        "with"
    ],
    "misspell": [
        "in"
    ],
    "roam": [
        "between",
        "to",
        "off",
        "on"
    ],
    "outgo": [
        "to"
    ],
    "overshoot": [
        "for"
    ],
    "park": [
        "until",
        "for",
        "in",
        "at"
    ],
    "placeholder": [
        "in"
    ],
    "pinch": [
        "by",
        "in",
        "out"
    ],
    "pollute": [
        "with"
    ],
    "prioritize": [
        "from",
        "by",
        "with",
        "on"
    ],
    "proof": [
        "with"
    ],
    "sneak": [
        "from"
    ],
    "reconnecting": [
        "in"
    ],
    "reinstate": [
        "as"
    ],
    "sprout": [
        "with"
    ],
    "off": [
        "off"
    ],
    "down": [
        "down"
    ],
    "settle": [
        "at",
        "down",
        "up"
    ],
    "slop": [
        "near"
    ],
    "stash": [
        "for",
        "with"
    ],
    "summarise": [
        "as"
    ],
    "proxied": [
        "on",
        "to",
        "with",
        "from"
    ],
    "underlie": [
        "with"
    ],
    "serialise": [
        "to"
    ],
    "weed": [
        "out"
    ],
    "tlv": [
        "to"
    ],
    "isis": [
        "up",
        "down"
    ],
    "iso639": [
        "to"
    ],
    "isoweekdate": [
        "to"
    ],
    "2d": [
        "at"
    ],
    "as": [
        "as"
    ],
    "over": [
        "over"
    ],
    "tooltip": [
        "to"
    ],
    "yellow": [
        "to"
    ],
    "sketch": [
        "to",
        "out"
    ],
    "jest": [
        "to"
    ],
    "jimplify": [
        "to"
    ],
    "jog": [
        "to"
    ],
    "joust": [
        "to"
    ],
    "ticket": [
        "to"
    ],
    "jso": [
        "to"
    ],
    "kg": [
        "to"
    ],
    "pound": [
        "to"
    ],
    "kit": [
        "to"
    ],
    "knock": [
        "from"
    ],
    "knot": [
        "at"
    ],
    "l7dlog": [
        "with",
        "without"
    ],
    "linger": [
        "before"
    ],
    "tokens": [
        "with",
        "inside",
        "outside"
    ],
    "lace": [
        "up"
    ],
    "lambdas": [
        "with"
    ],
    "landfall": [
        "under"
    ],
    "laplace": [
        "with"
    ],
    "headers": [
        "in",
        "on"
    ],
    "prime": [
        "to",
        "for"
    ],
    "any": [
        "of"
    ],
    "danger": [
        "on"
    ],
    "replenish": [
        "without"
    ],
    "leapfrog": [
        "with"
    ],
    "legend": [
        "off"
    ],
    "lighten": [
        "by"
    ],
    "lightter": [
        "by"
    ],
    "capacities": [
        "with"
    ],
    "responses": [
        "with"
    ],
    "modules": [
        "with"
    ],
    "usages": [
        "with",
        "in"
    ],
    "survey": [
        "for"
    ],
    "pint": [
        "to"
    ],
    "lob": [
        "in"
    ],
    "reconfigure": [
        "on",
        "by"
    ],
    "log10": [
        "to"
    ],
    "lon": [
        "to"
    ],
    "evr": [
        "by"
    ],
    "lop": [
        "off"
    ],
    "lpc": [
        "to",
        "in"
    ],
    "lprefc": [
        "to"
    ],
    "unlink": [
        "to",
        "from",
        "at",
        "with",
        "after"
    ],
    "reprojected": [
        "on",
        "up"
    ],
    "f1f": [
        "to"
    ],
    "dom": [
        "from"
    ],
    "self": [
        "by"
    ],
    "fop": [
        "to"
    ],
    "dao": [
        "to"
    ],
    "tuple": [
        "with"
    ],
    "acls": [
        "to"
    ],
    "marble": [
        "for"
    ],
    "marginalize": [
        "as"
    ],
    "ene": [
        "with"
    ],
    "roles": [
        "to",
        "in"
    ],
    "martyr": [
        "from"
    ],
    "massage": [
        "to"
    ],
    "rpc": [
        "off",
        "out",
        "of",
        "with",
        "up"
    ],
    "maxed": [
        "out"
    ],
    "resample": [
        "with"
    ],
    "rescue": [
        "into",
        "by"
    ],
    "resync": [
        "to"
    ],
    "mbcs": [
        "to"
    ],
    "wcs": [
        "to"
    ],
    "memoize": [
        "with",
        "at",
        "between",
        "from"
    ],
    "menu": [
        "with"
    ],
    "milliseconds": [
        "to"
    ],
    "sift": [
        "down",
        "up"
    ],
    "mistake": [
        "as"
    ],
    "mop": [
        "up"
    ],
    "all": [
        "by"
    ],
    "graveyard": [
        "with"
    ],
    "by": [
        "by"
    ],
    "fullscreen": [
        "in"
    ],
    "movq": [
        "to"
    ],
    "mulligan": [
        "down",
        "to"
    ],
    "murmur128": [
        "as"
    ],
    "muse": [
        "to",
        "from"
    ],
    "primitive": [
        "for"
    ],
    "execut": [
        "on"
    ],
    "reallocate": [
        "through",
        "in"
    ],
    "n1ql": [
        "to"
    ],
    "nadmin": [
        "with"
    ],
    "nag": [
        "about"
    ],
    "nanoseconds": [
        "to"
    ],
    "nap": [
        "at"
    ],
    "atom": [
        "with"
    ],
    "conf": [
        "as"
    ],
    "credentials": [
        "for"
    ],
    "d": [
        "to"
    ],
    "editor": [
        "on"
    ],
    "epoch": [
        "after"
    ],
    "compositing": [
        "over"
    ],
    "importer": [
        "with"
    ],
    "instantiator": [
        "of"
    ],
    "multi": [
        "in"
    ],
    "nth": [
        "out"
    ],
    "preferences": [
        "from"
    ],
    "quantile": [
        "with",
        "from"
    ],
    "rendezvous": [
        "with"
    ],
    "ret": [
        "by",
        "to",
        "from"
    ],
    "router": [
        "with"
    ],
    "since": [
        "since"
    ],
    "slider": [
        "to"
    ],
    "slim": [
        "to"
    ],
    "standalone": [
        "up",
        "down"
    ],
    "timer": [
        "with"
    ],
    "updater": [
        "for"
    ],
    "wizard": [
        "about",
        "to"
    ],
    "ari": [
        "with"
    ],
    "boundary": [
        "after"
    ],
    "unmapped": [
        "at",
        "for",
        "in"
    ],
    "deviate": [
        "by"
    ],
    "recv": [
        "down",
        "up"
    ],
    "rnd": [
        "from"
    ],
    "until": [
        "until"
    ],
    "up": [
        "up",
        "to"
    ],
    "weather": [
        "for"
    ],
    "nibble": [
        "to"
    ],
    "storages": [
        "for"
    ],
    "longer": [
        "at"
    ],
    "lowercase": [
        "with"
    ],
    "nominate": [
        "for"
    ],
    "perturb": [
        "with"
    ],
    "percentile": [
        "to"
    ],
    "nose": [
        "out"
    ],
    "loopback": [
        "across"
    ],
    "wipe": [
        "out",
        "with"
    ],
    "notch": [
        "to"
    ],
    "noupdate": [
        "on"
    ],
    "8s": [
        "to",
        "for"
    ],
    "roberts": [
        "down",
        "for",
        "up"
    ],
    "p3c": [
        "to"
    ],
    "p3p": [
        "to"
    ],
    "dd": [
        "to"
    ],
    "nsave": [
        "under"
    ],
    "nshade": [
        "down"
    ],
    "denorm": [
        "to"
    ],
    "ntlm": [
        "to"
    ],
    "unselect": [
        "in",
        "up",
        "by"
    ],
    "oget": [
        "in"
    ],
    "okay": [
        "to"
    ],
    "unlinking": [
        "from"
    ],
    "pathing": [
        "through"
    ],
    "powerring": [
        "up"
    ],
    "udunits": [
        "to"
    ],
    "perfect": [
        "to"
    ],
    "ordain": [
        "as"
    ],
    "ordinate": [
        "as"
    ],
    "ostream": [
        "from"
    ],
    "overrule": [
        "by"
    ],
    "errata": [
        "in"
    ],
    "padd": [
        "with"
    ],
    "pairwise": [
        "to"
    ],
    "parametized": [
        "as"
    ],
    "reparse": [
        "in"
    ],
    "snippet": [
        "by"
    ],
    "pem": [
        "to"
    ],
    "percolate": [
        "down",
        "up"
    ],
    "persian": [
        "with"
    ],
    "pertain": [
        "to"
    ],
    "pexpire": [
        "at"
    ],
    "phrase": [
        "for",
        "as"
    ],
    "piece": [
        "for",
        "to"
    ],
    "pig": [
        "to"
    ],
    "pilfer": [
        "by"
    ],
    "pinpoint": [
        "on"
    ],
    "plaintext": [
        "over"
    ],
    "please": [
        "on",
        "to"
    ],
    "redistribute": [
        "from"
    ],
    "reselecting": [
        "in"
    ],
    "preload": [
        "on"
    ],
    "premier": [
        "on"
    ],
    "ought": [
        "to"
    ],
    "beloning": [
        "to"
    ],
    "crc": [
        "to"
    ],
    "println": [
        "with"
    ],
    "importance": [
        "for"
    ],
    "adm": [
        "to",
        "for"
    ],
    "deps": [
        "in"
    ],
    "benefit": [
        "from",
        "on"
    ],
    "proportion": [
        "above"
    ],
    "roi": [
        "out"
    ],
    "seg": [
        "to",
        "with"
    ],
    "suppose": [
        "to"
    ],
    "purpose": [
        "of"
    ],
    "pyrrole": [
        "with"
    ],
    "quack": [
        "like"
    ],
    "quart": [
        "to"
    ],
    "propogated": [
        "to"
    ],
    "unassociate": [
        "with",
        "for",
        "from"
    ],
    "rap": [
        "in",
        "up"
    ],
    "re": [
        "by",
        "for"
    ],
    "resouce": [
        "with"
    ],
    "whitespaces": [
        "up",
        "to"
    ],
    "realign": [
        "to"
    ],
    "rear": [
        "on"
    ],
    "reauthenticate": [
        "on",
        "out"
    ],
    "recenter": [
        "to"
    ],
    "reconect": [
        "on"
    ],
    "reconstitute": [
        "for"
    ],
    "recovery01": [
        "on"
    ],
    "emanate": [
        "from"
    ],
    "squash": [
        "to"
    ],
    "unencrypted": [
        "to"
    ],
    "recycler": [
        "without"
    ],
    "redeclare": [
        "inside",
        "in"
    ],
    "redeem": [
        "to"
    ],
    "versioned": [
        "from",
        "off"
    ],
    "reevaluate": [
        "for"
    ],
    "reexamine": [
        "with"
    ],
    "refire": [
        "on"
    ],
    "coeffs": [
        "to"
    ],
    "reformat": [
        "with",
        "for"
    ],
    "pc": [
        "with"
    ],
    "reimage": [
        "with"
    ],
    "reinstall": [
        "to"
    ],
    "reinterpret": [
        "as"
    ],
    "reissue": [
        "with"
    ],
    "reiterate": [
        "to"
    ],
    "rtcp": [
        "to"
    ],
    "relayout": [
        "down"
    ],
    "relinquish": [
        "to"
    ],
    "relock": [
        "with"
    ],
    "relogin": [
        "from"
    ],
    "aliases": [
        "to"
    ],
    "remapped": [
        "from"
    ],
    "remixed": [
        "from"
    ],
    "renumber": [
        "in"
    ],
    "reparametrize": [
        "for"
    ],
    "repartition": [
        "by"
    ],
    "reproduce": [
        "of"
    ],
    "isremoved": [
        "from",
        "after"
    ],
    "blackbox": [
        "on"
    ],
    "assoc": [
        "between"
    ],
    "resizable": [
        "off"
    ],
    "timestamped": [
        "from"
    ],
    "restructure": [
        "to"
    ],
    "resubmit": [
        "with"
    ],
    "rethrown": [
        "on",
        "after"
    ],
    "retract": [
        "to"
    ],
    "revalidate": [
        "outside"
    ],
    "rewire": [
        "on",
        "for"
    ],
    "rgba4444": [
        "to"
    ],
    "rgba8888": [
        "to"
    ],
    "rl": [
        "to"
    ],
    "rline": [
        "to"
    ],
    "rmove": [
        "to"
    ],
    "rocket": [
        "up"
    ],
    "half": [
        "up"
    ],
    "rpv01": [
        "on"
    ],
    "rrcurve": [
        "to"
    ],
    "rsa": [
        "with"
    ],
    "runtest": [
        "to"
    ],
    "obs": [
        "with"
    ],
    "incremented": [
        "by"
    ],
    "targetting": [
        "for"
    ],
    "sched": [
        "from"
    ],
    "docs": [
        "out",
        "of"
    ],
    "scratch": [
        "in"
    ],
    "seem": [
        "like",
        "to",
        "in"
    ],
    "hub": [
        "out"
    ],
    "statsd": [
        "from",
        "with"
    ],
    "attachmentlist": [
        "up",
        "to"
    ],
    "authorlist": [
        "up",
        "to"
    ],
    "clusterlist": [
        "up",
        "to"
    ],
    "doodle": [
        "in"
    ],
    "implicit": [
        "down"
    ],
    "reside": [
        "in"
    ],
    "titlelist": [
        "up",
        "to"
    ],
    "wallpaper": [
        "to",
        "for"
    ],
    "shimmer": [
        "on",
        "off"
    ],
    "autocast": [
        "to"
    ],
    "instanciate": [
        "with"
    ],
    "liquid": [
        "below"
    ],
    "uphold": [
        "after"
    ],
    "shovel": [
        "in",
        "to",
        "out"
    ],
    "sieve": [
        "of"
    ],
    "unsigned": [
        "as"
    ],
    "simplex": [
        "to"
    ],
    "accoring": [
        "to"
    ],
    "slag": [
        "to"
    ],
    "slurp": [
        "in"
    ],
    "smack": [
        "to"
    ],
    "smoothen": [
        "at"
    ],
    "smp": [
        "to"
    ],
    "snake": [
        "to",
        "of"
    ],
    "sole": [
        "inside"
    ],
    "ents": [
        "to",
        "for"
    ],
    "speciate": [
        "until"
    ],
    "spike": [
        "in",
        "with"
    ],
    "spliterator": [
        "up",
        "to"
    ],
    "spoil": [
        "by"
    ],
    "spool": [
        "to"
    ],
    "squish": [
        "to"
    ],
    "wps": [
        "with",
        "from"
    ],
    "samp": [
        "over"
    ],
    "straighten": [
        "by"
    ],
    "strengthen": [
        "to"
    ],
    "stripe": [
        "by",
        "to"
    ],
    "subarray": [
        "with"
    ],
    "substract": [
        "from",
        "with"
    ],
    "suck": [
        "into"
    ],
    "suffer": [
        "from"
    ],
    "superimpose": [
        "by"
    ],
    "superpose": [
        "after",
        "at"
    ],
    "subselect": [
        "as",
        "in"
    ],
    "survive": [
        "in",
        "with"
    ],
    "symlink": [
        "to",
        "on"
    ],
    "synpred": [
        "to"
    ],
    "t3": [
        "to"
    ],
    "tango": [
        "to"
    ],
    "tar": [
        "for"
    ],
    "tarnish": [
        "in"
    ],
    "tee": [
        "with"
    ],
    "telecast": [
        "to",
        "of"
    ],
    "freq": [
        "in"
    ],
    "evend": [
        "with"
    ],
    "test001login": [
        "with"
    ],
    "test002login": [
        "with"
    ],
    "test004login": [
        "with"
    ],
    "test006create": [
        "with"
    ],
    "test006login": [
        "without",
        "with"
    ],
    "test08": [
        "before"
    ],
    "feb2000": [
        "to"
    ],
    "compete": [
        "for",
        "of"
    ],
    "test304": [
        "with"
    ],
    "1s": [
        "to",
        "for"
    ],
    "clipboard": [
        "with"
    ],
    "amplify": [
        "with"
    ],
    "auratouched": [
        "on"
    ],
    "cli": [
        "with",
        "in"
    ],
    "misparsed": [
        "as"
    ],
    "reattaching": [
        "on"
    ],
    "targetted": [
        "by"
    ],
    "isotopes": [
        "to",
        "for"
    ],
    "unmod": [
        "as"
    ],
    "geographic": [
        "on"
    ],
    "wif": [
        "with"
    ],
    "gmt": [
        "around"
    ],
    "completeted": [
        "for"
    ],
    "cordoned": [
        "off"
    ],
    "diskoffering": [
        "in"
    ],
    "registrars": [
        "at"
    ],
    "uncorrelated": [
        "in"
    ],
    "saml": [
        "to",
        "over",
        "on",
        "of"
    ],
    "undelete": [
        "on"
    ],
    "decremented": [
        "in"
    ],
    "focusable": [
        "in"
    ],
    "def": [
        "out"
    ],
    "groub": [
        "by",
        "with"
    ],
    "parquet": [
        "with"
    ],
    "borged": [
        "with"
    ],
    "unsets": [
        "as"
    ],
    "iris": [
        "to",
        "with"
    ],
    "pipelined": [
        "with",
        "to",
        "out",
        "of"
    ],
    "age": [
        "out"
    ],
    "maintenance": [
        "with"
    ],
    "radix": [
        "out",
        "of"
    ],
    "recieved": [
        "by"
    ],
    "s": [
        "at"
    ],
    "soulbound": [
        "with"
    ],
    "versioning": [
        "with",
        "from"
    ],
    "preloaded": [
        "for"
    ],
    "watermarks": [
        "during"
    ],
    "sizeof": [
        "with"
    ],
    "sourround": [
        "with",
        "for"
    ],
    "surraung": [
        "as",
        "in"
    ],
    "outweigh": [
        "of"
    ],
    "montreal": [
        "by"
    ],
    "undeclared": [
        "in"
    ],
    "testv8": [
        "in"
    ],
    "rolledover": [
        "by"
    ],
    "itialize": [
        "from"
    ],
    "testloop": [
        "until"
    ],
    "testremove": [
        "with",
        "from"
    ],
    "textpro": [
        "to"
    ],
    "textureless": [
        "off",
        "on"
    ],
    "everthing": [
        "to"
    ],
    "thumbmail": [
        "from"
    ],
    "thumbnail": [
        "from"
    ],
    "tid": [
        "to"
    ],
    "tidy": [
        "up"
    ],
    "tie": [
        "to"
    ],
    "tighten": [
        "after"
    ],
    "timevalue": [
        "to"
    ],
    "tos": [
        "into"
    ],
    "transcode": [
        "to"
    ],
    "transduce": [
        "to"
    ],
    "transf": [
        "to"
    ],
    "cookies": [
        "on"
    ],
    "transmute": [
        "to"
    ],
    "trawl": [
        "until"
    ],
    "tred": [
        "to"
    ],
    "trend": [
        "with"
    ],
    "trickle": [
        "down"
    ],
    "procceed": [
        "to"
    ],
    "shortcuts": [
        "for"
    ],
    "unarrived": [
        "of"
    ],
    "unblank": [
        "from"
    ],
    "uninvite": [
        "from"
    ],
    "unite": [
        "with"
    ],
    "nulling": [
        "out"
    ],
    "unordered": [
        "of"
    ],
    "unpause": [
        "on",
        "for"
    ],
    "unschedule": [
        "for"
    ],
    "unseal": [
        "near"
    ],
    "impurities": [
        "as"
    ],
    "lvl": [
        "to"
    ],
    "wet": [
        "as"
    ],
    "untake": [
        "with"
    ],
    "recieving": [
        "on"
    ],
    "untransform": [
        "to"
    ],
    "uppend": [
        "to"
    ],
    "upsampling": [
        "to"
    ],
    "stuff": [
        "into"
    ],
    "verse": [
        "to"
    ],
    "supplier": [
        "with"
    ],
    "visualize": [
        "with"
    ],
    "volley": [
        "to"
    ],
    "vpls": [
        "to",
        "for",
        "from"
    ],
    "sotred": [
        "as"
    ],
    "tobe": [
        "out",
        "of"
    ],
    "wander": [
        "off",
        "on"
    ],
    "shipmentroute": [
        "at"
    ],
    "wildcards": [
        "like"
    ],
    "wiggle": [
        "around"
    ],
    "impair": [
        "since"
    ],
    "worst": [
        "of"
    ],
    "writeln": [
        "with"
    ],
    "xget": [
        "from"
    ],
    "xor": [
        "with",
        "by",
        "off",
        "out"
    ],
    "tjp": [
        "off"
    ],
    "zrange": [
        "with"
    ],
    "zrevrange": [
        "with"
    ]
}