# -*- coding: utf-8 -*-

import json
from enum import Enum
from typing import Union, List
from dataclasses import dataclass, asdict


@dataclass
class CommandResult:
    output: str
    error: str
    exit_code: int


class SwipeDirection(str, Enum):
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"


class DisplayRotation(int, Enum):
    ROTATION_0 = 0
    ROTATION_90 = 1
    ROTATION_180 = 2
    ROTATION_270 = 3



class AppState:
    INIT = 0        # åˆ�å§‹åŒ–çŠ¶æ€�ï¼Œåº”ç”¨æ­£åœ¨åˆ�å§‹åŒ–
    READY = 1       # å°±ç»ªçŠ¶æ€�ï¼Œåº”ç”¨å·²åˆ�å§‹åŒ–å®Œæ¯•
    FOREGROUND = 2  # å‰�å�°çŠ¶æ€�ï¼Œåº”ç”¨ä½�äºŽå‰�å�°
    FOCUS = 3       # èŽ·ç„¦çŠ¶æ€�ã€‚ï¼ˆé¢„ç•™çŠ¶æ€�ï¼Œå½“å‰�æš‚ä¸�æ”¯æŒ�ï¼‰
    BACKGROUND = 4  # å�Žå�°çŠ¶æ€�ï¼Œåº”ç”¨ä½�äºŽå�Žå�°
    EXIT = 5        # é€€å‡ºçŠ¶æ€�ï¼Œåº”ç”¨å·²é€€å‡º


@dataclass
class DeviceInfo:
    productName: str
    model: str
    sdkVersion: str
    sysVersion: str
    cpuAbi: str
    wlanIp: str
    displaySize: tuple
    displayRotation: DisplayRotation


@dataclass
class HypiumResponse:
    """
    Example:
    {"result":"On#1"}
    {"result":null}
    {"result":null,"exception":"Can not connect to AAMS, RET_ERR_CONNECTION_EXIST"}
    {"exception":{"code":401,"message":"(PreProcessing: APiCallInfoChecker)Illegal argument count"}}
    """
    result: Union[List, bool, str, None] = None
    exception: Union[List, bool, str, None] = None


@dataclass
class ByData:
    value: str  # "On#0"


@dataclass
class DriverData:
    value: str   # "Driver#0"


@dataclass
class ComponentData:
    value: str  # "Component#0"


@dataclass
class Point:
    x: int
    y: int




@dataclass
class Bounds:
    left: int
    top: int
    right: int
    bottom: int



@dataclass
class ElementInfo:
    id: str
    key: str
    type: str
    text: str
    description: str
    isSelected: bool
    isChecked: bool
    isEnabled: bool
    isFocused: bool
    isCheckable: bool
    isClickable: bool
    isLongClickable: bool
    isScrollable: bool
    bounds: Bounds
    boundsCenter: Point

    def __str__(self) -> str:
        return json.dumps(asdict(self), indent=4)




class KeyCode(Enum):
    """
    Openharmonyé”®ç›˜ç �
    """
    FN = 0  # åŠŸèƒ½ï¼ˆFnï¼‰é”®
    UNKNOWN = -1  # æœªçŸ¥æŒ‰é”®
    HOME = 1  # åŠŸèƒ½ï¼ˆHomeï¼‰é”®
    BACK = 2  # è¿”å›žé”®
    MEDIA_PLAY_PAUSE = 10  # å¤šåª’ä½“é”®æ’­æ”¾/æš‚å�œ
    MEDIA_STOP = 11  # å¤šåª’ä½“é”®å�œæ­¢
    MEDIA_NEXT = 12  # å¤šåª’ä½“é”®ä¸‹ä¸€é¦–
    MEDIA_PREVIOUS = 13  # å¤šåª’ä½“é”®ä¸Šä¸€é¦–
    MEDIA_REWIND = 14  # å¤šåª’ä½“é”®å¿«é€€
    MEDIA_FAST_FORWARD = 15  # å¤šåª’ä½“é”®å¿«è¿›
    VOLUME_UP = 16  # éŸ³é‡�å¢žåŠ é”®
    VOLUME_DOWN = 17  # éŸ³é‡�å‡�å°�é”®
    POWER = 18  # ç”µæº�é”®
    CAMERA = 19  # æ‹�ç…§é”®
    VOLUME_MUTE = 22  # æ‰¬å£°å™¨é�™éŸ³é”®
    MUTE = 23  # è¯�ç­’é�™éŸ³é”®
    BRIGHTNESS_UP = 40  # äº®åº¦è°ƒèŠ‚æŒ‰é”®è°ƒäº®
    BRIGHTNESS_DOWN = 41  # äº®åº¦è°ƒèŠ‚æŒ‰é”®è°ƒæš—
    NUM_0 = 2000  # æŒ‰é”®â€™0â€™
    NUM_1 = 2001  # æŒ‰é”®â€™1â€™
    NUM_2 = 2002  # æŒ‰é”®â€™2â€™
    NUM_3 = 2003  # æŒ‰é”®â€™3â€™
    NUM_4 = 2004  # æŒ‰é”®â€™4â€™
    NUM_5 = 2005  # æŒ‰é”®â€™5â€™
    NUM_6 = 2006  # æŒ‰é”®â€™6â€™
    NUM_7 = 2007  # æŒ‰é”®â€™7â€™
    NUM_8 = 2008  # æŒ‰é”®â€™8â€™
    NUM_9 = 2009  # æŒ‰é”®â€™9â€™
    STAR = 2010  # æŒ‰é”®â€™*â€™
    POUND = 2011  # æŒ‰é”®â€™#â€™
    DPAD_UP = 2012  # å¯¼èˆªé”®å�‘ä¸Š
    DPAD_DOWN = 2013  # å¯¼èˆªé”®å�‘ä¸‹
    DPAD_LEFT = 2014  # å¯¼èˆªé”®å�‘å·¦
    DPAD_RIGHT = 2015  # å¯¼èˆªé”®å�‘å�³
    DPAD_CENTER = 2016  # å¯¼èˆªé”®ç¡®å®šé”®
    A = 2017  # æŒ‰é”®â€™Aâ€™
    B = 2018  # æŒ‰é”®â€™Bâ€™
    C = 2019  # æŒ‰é”®â€™Câ€™
    D = 2020  # æŒ‰é”®â€™Dâ€™
    E = 2021  # æŒ‰é”®â€™Eâ€™
    F = 2022  # æŒ‰é”®â€™Fâ€™
    G = 2023  # æŒ‰é”®â€™Gâ€™
    H = 2024  # æŒ‰é”®â€™Hâ€™
    I = 2025  # æŒ‰é”®â€™Iâ€™
    J = 2026  # æŒ‰é”®â€™Jâ€™
    K = 2027  # æŒ‰é”®â€™Kâ€™
    L = 2028  # æŒ‰é”®â€™Lâ€™
    M = 2029  # æŒ‰é”®â€™Mâ€™
    N = 2030  # æŒ‰é”®â€™Nâ€™
    O = 2031  # æŒ‰é”®â€™Oâ€™
    P = 2032  # æŒ‰é”®â€™Pâ€™
    Q = 2033  # æŒ‰é”®â€™Qâ€™
    R = 2034  # æŒ‰é”®â€™Râ€™
    S = 2035  # æŒ‰é”®â€™Sâ€™
    T = 2036  # æŒ‰é”®â€™Tâ€™
    U = 2037  # æŒ‰é”®â€™Uâ€™
    V = 2038  # æŒ‰é”®â€™Vâ€™
    W = 2039  # æŒ‰é”®â€™Wâ€™
    X = 2040  # æŒ‰é”®â€™Xâ€™
    Y = 2041  # æŒ‰é”®â€™Yâ€™
    Z = 2042  # æŒ‰é”®â€™Zâ€™
    COMMA = 2043  # æŒ‰é”®â€™,â€™
    PERIOD = 2044  # æŒ‰é”®â€™.â€™
    ALT_LEFT = 2045  # å·¦Alté”®
    ALT_RIGHT = 2046  # å�³Alté”®
    SHIFT_LEFT = 2047  # å·¦Shifté”®
    SHIFT_RIGHT = 2048  # å�³Shifté”®
    TAB = 2049  # Tabé”®
    SPACE = 2050  # ç©ºæ ¼é”®
    SYM = 2051  # ç¬¦å�·ä¿®æ”¹å™¨æŒ‰é”®
    EXPLORER = 2052  # æµ�è§ˆå™¨åŠŸèƒ½é”®ï¼Œæ­¤é”®ç”¨äºŽå�¯åŠ¨æµ�è§ˆå™¨åº”ç”¨ç¨‹åº�ã€‚
    ENVELOPE = 2053  # ç”µå­�é‚®ä»¶åŠŸèƒ½é”®ï¼Œæ­¤é”®ç”¨äºŽå�¯åŠ¨ç”µå­�é‚®ä»¶åº”ç”¨ç¨‹åº�ã€‚
    ENTER = 2054  # å›žè½¦é”®
    DEL = 2055  # é€€æ ¼é”®
    GRAVE = 2056  # æŒ‰é”®â€™`â€™
    MINUS = 2057  # æŒ‰é”®â€™-â€™
    EQUALS = 2058  # æŒ‰é”®â€™=â€™
    LEFT_BRACKET = 2059  # æŒ‰é”®â€™[â€™
    RIGHT_BRACKET = 2060  # æŒ‰é”®â€™]â€™
    BACKSLASH = 2061  # æŒ‰é”®â€™\â€™
    SEMICOLON = 2062  # æŒ‰é”®â€™;â€™
    APOSTROPHE = 2063  # æŒ‰é”®â€™â€˜â€™(å�•å¼•å�·)
    SLASH = 2064  # æŒ‰é”®â€™/â€™
    AT = 2065  # æŒ‰é”®â€™@â€™
    PLUS = 2066  # æŒ‰é”®â€™+â€™
    MENU = 2067  # è�œå�•é”®
    PAGE_UP = 2068  # å�‘ä¸Šç¿»é¡µé”®
    PAGE_DOWN = 2069  # å�‘ä¸‹ç¿»é¡µé”®
    ESCAPE = 2070  # ESCé”®
    FORWARD_DEL = 2071  # åˆ é™¤é”®
    CTRL_LEFT = 2072  # å·¦Ctrlé”®
    CTRL_RIGHT = 2073  # å�³Ctrlé”®
    CAPS_LOCK = 2074  # å¤§å†™é”�å®šé”®
    SCROLL_LOCK = 2075  # æ»šåŠ¨é”�å®šé”®
    META_LEFT = 2076  # å·¦å…ƒä¿®æ”¹å™¨é”®
    META_RIGHT = 2077  # å�³å…ƒä¿®æ”¹å™¨é”®
    FUNCTION = 2078  # åŠŸèƒ½é”®
    SYSRQ = 2079  # ç³»ç»Ÿè¯·æ±‚/æ‰“å�°å±�å¹•é”®
    BREAK = 2080  # Break/Pauseé”®
    MOVE_HOME = 2081  # å…‰æ ‡ç§»åŠ¨åˆ°å¼€å§‹é”®
    MOVE_END = 2082  # å…‰æ ‡ç§»åŠ¨åˆ°æœ«å°¾é”®
    INSERT = 2083  # æ�’å…¥é”®
    FORWARD = 2084  # å‰�è¿›é”®
    MEDIA_PLAY = 2085  # å¤šåª’ä½“é”®æ’­æ”¾
    MEDIA_PAUSE = 2086  # å¤šåª’ä½“é”®æš‚å�œ
    MEDIA_CLOSE = 2087  # å¤šåª’ä½“é”®å…³é—­
    MEDIA_EJECT = 2088  # å¤šåª’ä½“é”®å¼¹å‡º
    MEDIA_RECORD = 2089  # å¤šåª’ä½“é”®å½•éŸ³
    F1 = 2090  # æŒ‰é”®â€™F1â€™
    F2 = 2091  # æŒ‰é”®â€™F2â€™
    F3 = 2092  # æŒ‰é”®â€™F3â€™
    F4 = 2093  # æŒ‰é”®â€™F4â€™
    F5 = 2094  # æŒ‰é”®â€™F5â€™
    F6 = 2095  # æŒ‰é”®â€™F6â€™
    F7 = 2096  # æŒ‰é”®â€™F7â€™
    F8 = 2097  # æŒ‰é”®â€™F8â€™
    F9 = 2098  # æŒ‰é”®â€™F9â€™
    F10 = 2099  # æŒ‰é”®â€™F10â€™
    F11 = 2100  # æŒ‰é”®â€™F11â€™
    F12 = 2101  # æŒ‰é”®â€™F12â€™
    NUM_LOCK = 2102  # å°�é”®ç›˜é”�
    NUMPAD_0 = 2103  # å°�é”®ç›˜æŒ‰é”®â€™0â€™
    NUMPAD_1 = 2104  # å°�é”®ç›˜æŒ‰é”®â€™1â€™
    NUMPAD_2 = 2105  # å°�é”®ç›˜æŒ‰é”®â€™2â€™
    NUMPAD_3 = 2106  # å°�é”®ç›˜æŒ‰é”®â€™3â€™
    NUMPAD_4 = 2107  # å°�é”®ç›˜æŒ‰é”®â€™4â€™
    NUMPAD_5 = 2108  # å°�é”®ç›˜æŒ‰é”®â€™5â€™
    NUMPAD_6 = 2109  # å°�é”®ç›˜æŒ‰é”®â€™6â€™
    NUMPAD_7 = 2110  # å°�é”®ç›˜æŒ‰é”®â€™7â€™
    NUMPAD_8 = 2111  # å°�é”®ç›˜æŒ‰é”®â€™8â€™
    NUMPAD_9 = 2112  # å°�é”®ç›˜æŒ‰é”®â€™9â€™
    NUMPAD_DIVIDE = 2113  # å°�é”®ç›˜æŒ‰é”®â€™/â€™
    NUMPAD_MULTIPLY = 2114  # å°�é”®ç›˜æŒ‰é”®â€™*â€™
    NUMPAD_SUBTRACT = 2115  # å°�é”®ç›˜æŒ‰é”®â€™-â€™
    NUMPAD_ADD = 2116  # å°�é”®ç›˜æŒ‰é”®â€™+â€™
    NUMPAD_DOT = 2117  # å°�é”®ç›˜æŒ‰é”®â€™.â€™
    NUMPAD_COMMA = 2118  # å°�é”®ç›˜æŒ‰é”®â€™,â€™
    NUMPAD_ENTER = 2119  # å°�é”®ç›˜æŒ‰é”®å›žè½¦
    NUMPAD_EQUALS = 2120  # å°�é”®ç›˜æŒ‰é”®â€™=â€™
    NUMPAD_LEFT_PAREN = 2121  # å°�é”®ç›˜æŒ‰é”®â€™(â€™
    NUMPAD_RIGHT_PAREN = 2122  # å°�é”®ç›˜æŒ‰é”®â€™)â€™
    VIRTUAL_MULTITASK = 2210  # è™šæ‹Ÿå¤šä»»åŠ¡é”®
    SLEEP = 2600  # ç�¡çœ é”®
    ZENKAKU_HANKAKU = 2601  # æ—¥æ–‡å…¨å®½/å�Šå®½é”®
    ND = 2602  # 102ndæŒ‰é”®
    RO = 2603  # æ—¥æ–‡Roé”®
    KATAKANA = 2604  # æ—¥æ–‡ç‰‡å�‡å��é”®
    HIRAGANA = 2605  # æ—¥æ–‡å¹³å�‡å��é”®
    HENKAN = 2606  # æ—¥æ–‡è½¬æ�¢é”®
    KATAKANA_HIRAGANA = 2607  # æ—¥è¯­ç‰‡å�‡å��/å¹³å�‡å��é”®
    MUHENKAN = 2608  # æ—¥æ–‡é�žè½¬æ�¢é”®
    LINEFEED = 2609  # æ�¢è¡Œé”®
    MACRO = 2610  # å®�é”®
    NUMPAD_PLUSMINUS = 2611  # æ•°å­—é”®ç›˜ä¸Šçš„åŠ å�·/å‡�å�·é”®
    SCALE = 2612  # æ‰©å±•é”®
    HANGUEL = 2613  # æ—¥æ–‡éŸ©è¯­é”®
    HANJA = 2614  # æ—¥æ–‡æ±‰è¯­é”®
    YEN = 2615  # æ—¥å…ƒé”®
    STOP = 2616  # å�œæ­¢é”®
    AGAIN = 2617  # é‡�å¤�é”®
    PROPS = 2618  # é�“å…·é”®
    UNDO = 2619  # æ’¤æ¶ˆé”®
    COPY = 2620  # å¤�åˆ¶é”®
    OPEN = 2621  # æ‰“å¼€é”®
    PASTE = 2622  # ç²˜è´´é”®
    FIND = 2623  # æŸ¥æ‰¾é”®
    CUT = 2624  # å‰ªåˆ‡é”®
    HELP = 2625  # å¸®åŠ©é”®
    CALC = 2626  # è®¡ç®—å™¨ç‰¹æ®ŠåŠŸèƒ½é”®ï¼Œç”¨äºŽå�¯åŠ¨è®¡ç®—å™¨åº”ç”¨ç¨‹åº�
    FILE = 2627  # æ–‡ä»¶æŒ‰é”®
    BOOKMARKS = 2628  # ä¹¦ç­¾é”®
    NEXT = 2629  # ä¸‹ä¸€ä¸ªæŒ‰é”®
    PLAYPAUSE = 2630  # æ’­æ”¾/æš‚å�œé”®
    PREVIOUS = 2631  # ä¸Šä¸€ä¸ªæŒ‰é”®
    STOPCD = 2632  # CDå�œæ­¢é”®
    CONFIG = 2634  # é…�ç½®é”®
    REFRESH = 2635  # åˆ·æ–°é”®
    EXIT = 2636  # é€€å‡ºé”®
    EDIT = 2637  # ç¼–è¾‘é”®
    SCROLLUP = 2638  # å�‘ä¸Šæ»šåŠ¨é”®
    SCROLLDOWN = 2639  # å�‘ä¸‹æ»šåŠ¨é”®
    NEW = 2640  # æ–°å»ºé”®
    REDO = 2641  # æ�¢å¤�é”®
    CLOSE = 2642  # å…³é—­é”®
    PLAY = 2643  # æ’­æ”¾é”®
    BASSBOOST = 2644  # ä½ŽéŸ³å¢žå¼ºé”®
    PRINT = 2645  # æ‰“å�°é”®
    CHAT = 2646  # è�Šå¤©é”®
    FINANCE = 2647  # é‡‘èž�é”®
    CANCEL = 2648  # å�–æ¶ˆé”®
    KBDILLUM_TOGGLE = 2649  # é”®ç›˜ç�¯å…‰åˆ‡æ�¢é”®
    KBDILLUM_DOWN = 2650  # é”®ç›˜ç�¯å…‰è°ƒäº®é”®
    KBDILLUM_UP = 2651  # é”®ç›˜ç�¯å…‰è°ƒæš—é”®
    SEND = 2652  # å�‘é€�é”®
    REPLY = 2653  # ç­”å¤�é”®
    FORWARDMAIL = 2654  # é‚®ä»¶è½¬å�‘é”®
    SAVE = 2655  # ä¿�å­˜é”®
    DOCUMENTS = 2656  # æ–‡ä»¶é”®
    VIDEO_NEXT = 2657  # ä¸‹ä¸€ä¸ªè§†é¢‘é”®
    VIDEO_PREV = 2658  # ä¸Šä¸€ä¸ªè§†é¢‘é”®
    BRIGHTNESS_CYCLE = 2659  # èƒŒå…‰æ¸�å�˜é”®
    BRIGHTNESS_ZERO = 2660  # äº®åº¦è°ƒèŠ‚ä¸º0é”®
    DISPLAY_OFF = 2661  # æ˜¾ç¤ºå…³é—­é”®
    BTN_MISC = 2662  # æ¸¸æˆ�æ‰‹æŸ„ä¸Šçš„å�„ç§�æŒ‰é”®
    GOTO = 2663  # è¿›å…¥é”®
    INFO = 2664  # ä¿¡æ�¯æŸ¥çœ‹é”®
    PROGRAM = 2665  # ç¨‹åº�é”®
    PVR = 2666  # ä¸ªäººå½•åƒ�æœº(PVR)é”®
    SUBTITLE = 2667  # å­—å¹•é”®
    FULL_SCREEN = 2668  # å…¨å±�é”®
    KEYBOARD = 2669  # é”®ç›˜
    ASPECT_RATIO = 2670  # å±�å¹•çºµæ¨ªæ¯”è°ƒèŠ‚é”®
    PC = 2671  # ç«¯å�£æŽ§åˆ¶é”®
    TV = 2672  # TVé”®
    TV2 = 2673  # TVé”®2
    VCR = 2674  # å½•åƒ�æœºå¼€å�¯é”®
    VCR2 = 2675  # å½•åƒ�æœºå¼€å�¯é”®2
    SAT = 2676  # SIMå�¡åº”ç”¨å·¥å…·åŒ…ï¼ˆSATï¼‰é”®
    CD = 2677  # CDé”®
    TAPE = 2678  # ç£�å¸¦é”®
    TUNER = 2679  # è°ƒè°�å™¨é”®
    PLAYER = 2680  # æ’­æ”¾å™¨é”®
    DVD = 2681  # DVDé”®
    AUDIO = 2682  # éŸ³é¢‘é”®
    VIDEO = 2683  # è§†é¢‘é”®
    MEMO = 2684  # å¤‡å¿˜å½•é”®
    CALENDAR = 2685  # æ—¥åŽ†é”®
    RED = 2686  # çº¢è‰²æŒ‡ç¤ºå™¨
    GREEN = 2687  # ç»¿è‰²æŒ‡ç¤ºå™¨
    YELLOW = 2688  # é»„è‰²æŒ‡ç¤ºå™¨
    BLUE = 2689  # è“�è‰²æŒ‡ç¤ºå™¨
    CHANNELUP = 2690  # é¢‘é�“å�‘ä¸Šé”®
    CHANNELDOWN = 2691  # é¢‘é�“å�‘ä¸‹é”®
    LAST = 2692  # æœ«å°¾é”®
    RESTART = 2693  # é‡�å�¯é”®
    SLOW = 2694  # æ…¢é€Ÿé”®
    SHUFFLE = 2695  # éš�æœºæ’­æ”¾é”®
    VIDEOPHONE = 2696  # å�¯è§†ç”µè¯�é”®
    GAMES = 2697  # æ¸¸æˆ�é”®
    ZOOMIN = 2698  # æ”¾å¤§é”®
    ZOOMOUT = 2699  # ç¼©å°�é”®
    ZOOMRESET = 2700  # ç¼©æ”¾é‡�ç½®é”®
    WORDPROCESSOR = 2701  # æ–‡å­—å¤„ç�†é”®
    EDITOR = 2702  # ç¼–è¾‘å™¨é”®
    SPREADSHEET = 2703  # ç”µå­�è¡¨æ ¼é”®
    GRAPHICSEDITOR = 2704  # å›¾å½¢ç¼–è¾‘å™¨é”®
    PRESENTATION = 2705  # æ¼”ç¤ºæ–‡ç¨¿é”®
    DATABASE = 2706  # æ•°æ�®åº“é”®æ ‡
    NEWS = 2707  # æ–°é—»é”®
    VOICEMAIL = 2708  # è¯­éŸ³ä¿¡ç®±
    ADDRESSBOOK = 2709  # é€šè®¯ç°¿
    MESSENGER = 2710  # é€šä¿¡é”®
    BRIGHTNESS_TOGGLE = 2711  # äº®åº¦åˆ‡æ�¢é”®
    SPELLCHECK = 2712  # ALæ‹¼å†™æ£€æŸ¥
    COFFEE = 2713  # ç»ˆç«¯é”�/å±�å¹•ä¿�æŠ¤ç¨‹åº�
    MEDIA_REPEAT = 2714  # åª’ä½“å¾ªçŽ¯é”®
    IMAGES = 2715  # å›¾åƒ�é”®
    BUTTONCONFIG = 2716  # æŒ‰é”®é…�ç½®é”®
    TASKMANAGER = 2717  # ä»»åŠ¡ç®¡ç�†å™¨
    JOURNAL = 2718  # æ—¥å¿—æŒ‰é”®
    CONTROLPANEL = 2719  # æŽ§åˆ¶é�¢æ�¿é”®
    APPSELECT = 2720  # åº”ç”¨ç¨‹åº�é€‰æ‹©é”®
    SCREENSAVER = 2721  # å±�å¹•ä¿�æŠ¤ç¨‹åº�é”®
    ASSISTANT = 2722  # è¾…åŠ©é”®
    KBD_LAYOUT_NEXT = 2723  # ä¸‹ä¸€ä¸ªé”®ç›˜å¸ƒå±€é”®
    BRIGHTNESS_MIN = 2724  # æœ€å°�äº®åº¦é”®
    BRIGHTNESS_MAX = 2725  # æœ€å¤§äº®åº¦é”®
    KBDINPUTASSIST_PREV = 2726  # é”®ç›˜è¾“å…¥Assist_Previous
    KBDINPUTASSIST_NEXT = 2727  # é”®ç›˜è¾“å…¥Assist_Next
    KBDINPUTASSIST_PREVGROUP = 2728  # é”®ç›˜è¾“å…¥Assist_Previous
    KBDINPUTASSIST_NEXTGROUP = 2729  # é”®ç›˜è¾“å…¥Assist_Next
    KBDINPUTASSIST_ACCEPT = 2730  # é”®ç›˜è¾“å…¥Assist_Accept
    KBDINPUTASSIST_CANCEL = 2731  # é”®ç›˜è¾“å…¥Assist_Cancel
    FRONT = 2800  # æŒ¡é£ŽçŽ»ç’ƒé™¤é›¾å™¨å¼€å…³
    SETUP = 2801  # è®¾ç½®é”®
    WAKE_UP = 2802  # å”¤é†’é”®
    SENDFILE = 2803  # å�‘é€�æ–‡ä»¶æŒ‰é”®
    DELETEFILE = 2804  # åˆ é™¤æ–‡ä»¶æŒ‰é”®
    XFER = 2805  # æ–‡ä»¶ä¼ è¾“(XFER)æŒ‰é”®
    PROG1 = 2806  # ç¨‹åº�é”®1
    PROG2 = 2807  # ç¨‹åº�é”®2
    MSDOS = 2808  # MS-DOSé”®ï¼ˆå¾®è½¯ç£�ç›˜æ“�ä½œç³»ç»Ÿ
    SCREENLOCK = 2809  # å±�å¹•é”�å®šé”®
    DIRECTION_ROTATE_DISPLAY = 2810  # æ–¹å�‘æ—‹è½¬æ˜¾ç¤ºé”®
    CYCLEWINDOWS = 2811  # Windowså¾ªçŽ¯é”®
    COMPUTER = 2812  # æŒ‰é”®
    EJECTCLOSECD = 2813  # å¼¹å‡ºCDé”®
    ISO = 2814  # ISOé”®
    MOVE = 2815  # ç§»åŠ¨é”®
    F13 = 2816  # æŒ‰é”®â€™F13â€™
    F14 = 2817  # æŒ‰é”®â€™F14â€™
    F15 = 2818  # æŒ‰é”®â€™F15â€™
    F16 = 2819  # æŒ‰é”®â€™F16â€™
    F17 = 2820  # æŒ‰é”®â€™F17â€™
    F18 = 2821  # æŒ‰é”®â€™F18â€™
    F19 = 2822  # æŒ‰é”®â€™F19â€™
    F20 = 2823  # æŒ‰é”®â€™F20â€™
    F21 = 2824  # æŒ‰é”®â€™F21â€™
    F22 = 2825  # æŒ‰é”®â€™F22â€™
    F23 = 2826  # æŒ‰é”®â€™F23â€™
    F24 = 2827  # æŒ‰é”®â€™F24â€™
    PROG3 = 2828  # ç¨‹åº�é”®3
    PROG4 = 2829  # ç¨‹åº�é”®4
    DASHBOARD = 2830  # ä»ªè¡¨æ�¿
    SUSPEND = 2831  # æŒ‚èµ·é”®
    HP = 2832  # é«˜é˜¶è·¯å¾„é”®
    SOUND = 2833  # éŸ³é‡�é”®
    QUESTION = 2834  # ç–‘é—®æŒ‰é”®
    CONNECT = 2836  # è¿žæŽ¥é”®
    SPORT = 2837  # è¿�åŠ¨æŒ‰é”®
    SHOP = 2838  # å•†åŸŽé”®
    ALTERASE = 2839  # äº¤æ›¿é”®
    SWITCHVIDEOMODE = 2841  # åœ¨å�¯ç”¨è§†é¢‘ä¹‹é—´å¾ªçŽ¯è¾“å‡ºï¼ˆç›‘è§†å™¨/LCD/TVè¾“å‡º/ç­‰ï¼‰
    BATTERY = 2842  # ç”µæ± æŒ‰é”®
    BLUETOOTH = 2843  # è“�ç‰™æŒ‰é”®
    WLAN = 2844  # æ— çº¿å±€åŸŸç½‘
    UWB = 2845  # è¶…å®½å¸¦ï¼ˆUWBï¼‰
    WWAN_WIMAX = 2846  # WWANWiMAXæŒ‰é”®
    RFKILL = 2847  # æŽ§åˆ¶æ‰€æœ‰æ”¶éŸ³æœºçš„é”®
    CHANNEL = 3001  # å�‘ä¸Šé¢‘é�“é”®
    BTN_0 = 3100  # æŒ‰é”®0
    BTN_1 = 3101  # æŒ‰é”®1
    BTN_2 = 3102  # æŒ‰é”®2
    BTN_3 = 3103  # æŒ‰é”®3
    BTN_4 = 3104  # æŒ‰é”®4
    BTN_5 = 3105  # æŒ‰é”®5
    BTN_6 = 3106  # æŒ‰é”®6
    BTN_7 = 3107  # æŒ‰é”®7
    BTN_8 = 3108  # æŒ‰é”®8
    BTN_9 = 3109  # æŒ‰é”®9