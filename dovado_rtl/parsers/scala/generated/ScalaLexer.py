# Generated from Scala.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,78,805,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,
        91,7,91,2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,7,
        97,2,98,7,98,2,99,7,99,2,100,7,100,2,101,7,101,2,102,7,102,2,103,
        7,103,2,104,7,104,2,105,7,105,2,106,7,106,2,107,7,107,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,
        1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,
        1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,24,1,24,
        1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,
        1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,29,
        1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,
        1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,34,1,34,
        1,34,1,34,1,34,1,34,1,35,1,35,1,36,1,36,1,37,1,37,1,38,1,38,1,38,
        1,38,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,41,1,41,1,41,1,41,
        1,41,1,42,1,42,1,43,1,43,1,44,1,44,1,44,1,45,1,45,1,45,1,46,1,46,
        1,46,1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,
        1,48,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,50,1,50,1,50,
        1,50,1,50,1,50,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,52,1,52,1,52,
        1,52,1,52,1,52,1,52,1,52,1,53,1,53,1,53,1,53,1,53,1,53,1,53,1,53,
        1,53,1,53,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,55,1,55,1,55,1,55,
        1,56,1,56,1,56,1,56,1,56,1,56,1,57,1,57,1,57,1,57,1,57,1,57,1,57,
        1,58,1,58,1,58,1,58,1,58,1,58,1,59,1,59,1,59,1,59,1,59,1,59,1,59,
        1,59,1,60,1,60,1,60,1,60,1,60,1,60,1,60,1,60,1,61,1,61,1,61,1,61,
        1,61,4,61,500,8,61,11,61,12,61,501,1,61,1,61,3,61,506,8,61,1,62,
        1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,62,3,62,517,8,62,1,63,1,63,
        1,63,3,63,522,8,63,1,63,1,63,1,64,1,64,1,64,1,65,1,65,3,65,531,8,
        65,1,65,3,65,534,8,65,1,66,1,66,5,66,538,8,66,10,66,12,66,541,9,
        66,1,66,1,66,1,66,1,66,1,66,1,66,1,66,1,66,1,66,1,66,3,66,553,8,
        66,1,67,4,67,556,8,67,11,67,12,67,557,1,67,1,67,4,67,562,8,67,11,
        67,12,67,563,1,67,3,67,567,8,67,1,67,3,67,570,8,67,1,67,1,67,4,67,
        574,8,67,11,67,12,67,575,1,67,3,67,579,8,67,1,67,3,67,582,8,67,1,
        67,1,67,1,67,3,67,587,8,67,1,67,4,67,590,8,67,11,67,12,67,591,1,
        67,3,67,595,8,67,1,67,1,67,3,67,599,8,67,1,68,1,68,1,68,1,69,1,69,
        1,69,1,69,1,69,3,69,609,8,69,1,70,1,70,1,71,1,71,1,72,1,72,4,72,
        617,8,72,11,72,12,72,618,3,72,621,8,72,1,72,1,72,1,73,1,73,1,73,
        3,73,628,8,73,3,73,630,8,73,1,74,1,74,1,75,1,75,1,75,3,75,637,8,
        75,1,75,1,75,1,75,1,75,1,75,1,76,1,76,1,77,1,77,1,78,3,78,649,8,
        78,1,78,4,78,652,8,78,11,78,12,78,653,1,79,1,79,5,79,658,8,79,10,
        79,12,79,661,9,79,1,79,1,79,3,79,665,8,79,1,80,1,80,3,80,669,8,80,
        1,81,1,81,5,81,673,8,81,10,81,12,81,676,9,81,1,82,1,82,1,83,1,83,
        1,84,1,84,3,84,684,8,84,1,85,1,85,3,85,688,8,85,1,86,1,86,1,86,1,
        86,3,86,694,8,86,1,87,1,87,3,87,698,8,87,1,87,4,87,701,8,87,11,87,
        12,87,702,1,88,1,88,1,89,1,89,1,90,1,90,1,90,1,91,1,91,1,91,5,91,
        715,8,91,10,91,12,91,718,9,91,3,91,720,8,91,1,92,1,92,1,92,1,92,
        4,92,726,8,92,11,92,12,92,727,1,93,1,93,3,93,732,8,93,1,94,1,94,
        1,95,1,95,1,96,1,96,1,96,1,96,1,96,1,96,1,96,3,96,745,8,96,1,97,
        1,97,1,97,1,97,1,97,3,97,752,8,97,1,98,1,98,1,99,1,99,1,100,1,100,
        1,101,1,101,1,102,1,102,1,103,1,103,1,104,4,104,767,8,104,11,104,
        12,104,768,1,104,1,104,1,105,4,105,774,8,105,11,105,12,105,775,1,
        105,1,105,1,106,1,106,1,106,1,106,1,106,5,106,785,8,106,10,106,12,
        106,788,9,106,1,106,1,106,1,106,1,106,1,106,1,107,1,107,1,107,1,
        107,5,107,799,8,107,10,107,12,107,802,9,107,1,107,1,107,0,0,108,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,
        27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,
        49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,
        71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,46,
        93,47,95,48,97,49,99,50,101,51,103,52,105,53,107,54,109,55,111,56,
        113,57,115,58,117,59,119,60,121,61,123,62,125,63,127,64,129,65,131,
        66,133,67,135,68,137,69,139,70,141,71,143,72,145,73,147,74,149,0,
        151,0,153,0,155,0,157,0,159,0,161,0,163,0,165,0,167,0,169,0,171,
        0,173,0,175,0,177,0,179,0,181,0,183,0,185,0,187,0,189,0,191,0,193,
        0,195,0,197,0,199,0,201,0,203,0,205,0,207,0,209,75,211,76,213,77,
        215,78,1,0,20,2,0,76,76,108,108,5,0,40,41,91,91,93,93,123,123,125,
        125,6,0,34,34,39,39,44,44,46,46,59,59,96,96,2,0,32,38,40,126,3,0,
        9,10,13,13,32,32,11,0,33,33,35,35,37,38,42,43,45,45,58,58,60,64,
        92,92,94,94,124,124,126,126,2,0,32,33,35,127,3,0,48,57,65,70,97,
        102,4,0,68,68,70,70,100,100,102,102,3,0,36,36,65,90,95,95,2,0,69,
        69,101,101,2,0,43,43,45,45,8,0,34,34,39,39,92,92,98,98,102,102,110,
        110,114,114,116,116,82,0,65,90,192,214,216,222,256,310,313,327,330,
        381,385,386,388,395,398,401,403,404,406,408,412,413,415,416,418,
        425,428,435,437,444,452,461,463,475,478,494,497,500,502,504,506,
        562,570,571,573,574,577,582,584,590,880,882,886,895,902,906,908,
        929,931,939,975,980,984,1006,1012,1015,1017,1018,1021,1071,1120,
        1152,1162,1229,1232,1326,1329,1366,4256,4293,4295,4301,7680,7828,
        7838,7934,7944,7951,7960,7965,7976,7983,7992,7999,8008,8013,8025,
        8031,8040,8047,8120,8123,8136,8139,8152,8155,8168,8172,8184,8187,
        8450,8455,8459,8461,8464,8466,8469,8477,8484,8493,8496,8499,8510,
        8511,8517,8579,11264,11310,11360,11364,11367,11376,11378,11381,11390,
        11392,11394,11490,11499,11501,11506,42560,42562,42604,42624,42650,
        42786,42798,42802,42862,42873,42886,42891,42893,42896,42898,42902,
        42925,42928,42929,65313,65338,81,0,97,122,181,246,248,255,257,375,
        378,384,387,389,392,402,405,411,414,417,419,421,424,429,432,436,
        438,447,454,460,462,499,501,505,507,569,572,578,583,659,661,687,
        881,883,887,893,912,974,976,977,981,983,985,1011,1013,1119,1121,
        1153,1163,1215,1218,1327,1377,1415,7424,7467,7531,7543,7545,7578,
        7681,7837,7839,7943,7952,7957,7968,7975,7984,7991,8000,8005,8016,
        8023,8032,8039,8048,8061,8064,8071,8080,8087,8096,8103,8112,8116,
        8118,8119,8126,8132,8134,8135,8144,8147,8150,8151,8160,8167,8178,
        8180,8182,8183,8458,8467,8495,8505,8508,8509,8518,8521,8526,8580,
        11312,11358,11361,11372,11377,11387,11393,11500,11502,11507,11520,
        11557,11559,11565,42561,42605,42625,42651,42787,42801,42803,42872,
        42874,42876,42879,42887,42892,42894,42897,42901,42903,42921,43002,
        43866,43876,43877,64256,64262,64275,64279,65345,65370,6,0,453,459,
        498,8079,8088,8095,8104,8111,8124,8140,8188,8188,33,0,688,705,710,
        721,736,740,748,750,884,890,1369,1600,1765,1766,2036,2037,2042,2074,
        2084,2088,2417,3654,3782,4348,6103,6211,6823,7293,7468,7530,7544,
        7615,8305,8319,8336,8348,11388,11389,11631,11823,12293,12341,12347,
        12542,40981,42237,42508,42623,42652,42653,42775,42783,42864,42888,
        43000,43001,43471,43494,43632,43741,43763,43764,43868,43871,65392,
        65439,234,0,170,186,443,451,660,1514,1520,1522,1568,1599,1601,1610,
        1646,1647,1649,1747,1749,1788,1791,1808,1810,1839,1869,1957,1969,
        2026,2048,2069,2112,2136,2208,2226,2308,2361,2365,2384,2392,2401,
        2418,2432,2437,2444,2447,2448,2451,2472,2474,2480,2482,2489,2493,
        2510,2524,2525,2527,2529,2544,2545,2565,2570,2575,2576,2579,2600,
        2602,2608,2610,2611,2613,2614,2616,2617,2649,2652,2654,2676,2693,
        2701,2703,2705,2707,2728,2730,2736,2738,2739,2741,2745,2749,2768,
        2784,2785,2821,2828,2831,2832,2835,2856,2858,2864,2866,2867,2869,
        2873,2877,2913,2929,2947,2949,2954,2958,2960,2962,2965,2969,2970,
        2972,2986,2990,3001,3024,3084,3086,3088,3090,3112,3114,3129,3133,
        3212,3214,3216,3218,3240,3242,3251,3253,3257,3261,3294,3296,3297,
        3313,3314,3333,3340,3342,3344,3346,3386,3389,3406,3424,3425,3450,
        3455,3461,3478,3482,3505,3507,3515,3517,3526,3585,3632,3634,3635,
        3648,3653,3713,3714,3716,3722,3725,3735,3737,3743,3745,3747,3749,
        3751,3754,3755,3757,3760,3762,3763,3773,3780,3804,3807,3840,3911,
        3913,3948,3976,3980,4096,4138,4159,4181,4186,4189,4193,4208,4213,
        4225,4238,4346,4349,4680,4682,4685,4688,4694,4696,4701,4704,4744,
        4746,4749,4752,4784,4786,4789,4792,4798,4800,4805,4808,4822,4824,
        4880,4882,4885,4888,4954,4992,5007,5024,5108,5121,5740,5743,5759,
        5761,5786,5792,5866,5873,5880,5888,5900,5902,5905,5920,5937,5952,
        5969,5984,5996,5998,6000,6016,6067,6108,6210,6212,6263,6272,6312,
        6314,6389,6400,6430,6480,6509,6512,6516,6528,6571,6593,6599,6656,
        6678,6688,6740,6917,6963,6981,6987,7043,7072,7086,7087,7098,7141,
        7168,7203,7245,7247,7258,7287,7401,7404,7406,7409,7413,7414,8501,
        8504,11568,11623,11648,11670,11680,11686,11688,11694,11696,11702,
        11704,11710,11712,11718,11720,11726,11728,11734,11736,11742,12294,
        12348,12353,12438,12447,12538,12543,12589,12593,12686,12704,12730,
        12784,12799,13312,19893,19968,40908,40960,40980,40982,42124,42192,
        42231,42240,42507,42512,42527,42538,42539,42606,42725,42999,43009,
        43011,43013,43015,43018,43020,43042,43072,43123,43138,43187,43250,
        43255,43259,43301,43312,43334,43360,43388,43396,43442,43488,43492,
        43495,43503,43514,43518,43520,43560,43584,43586,43588,43595,43616,
        43631,43633,43638,43642,43695,43697,43709,43712,43714,43739,43740,
        43744,43754,43762,43782,43785,43790,43793,43798,43808,43814,43816,
        43822,43968,44002,44032,55203,55216,55238,55243,55291,63744,64109,
        64112,64217,64285,64296,64298,64310,64312,64316,64318,64433,64467,
        64829,64848,64911,64914,64967,65008,65019,65136,65140,65142,65276,
        65382,65391,65393,65437,65440,65470,65474,65479,65482,65487,65490,
        65495,65498,65500,37,0,48,57,1632,1641,1776,1785,1984,1993,2406,
        2415,2534,2543,2662,2671,2790,2799,2918,2927,3046,3055,3174,3183,
        3302,3311,3430,3439,3558,3567,3664,3673,3792,3801,3872,3881,4160,
        4169,4240,4249,6112,6121,6160,6169,6470,6479,6608,6617,6784,6793,
        6800,6809,6992,7001,7088,7097,7232,7241,7248,7257,42528,42537,43216,
        43225,43264,43273,43472,43481,43504,43513,43600,43609,44016,44025,
        65296,65305,2,0,10,10,13,13,833,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,
        0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,
        0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,
        0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,
        0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,
        0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,
        0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,
        0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,
        0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,
        0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,
        0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,
        115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,
        0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,133,
        1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,0,0,0,141,1,0,0,0,
        0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,209,1,0,0,0,0,211,1,
        0,0,0,0,213,1,0,0,0,0,215,1,0,0,0,1,217,1,0,0,0,3,219,1,0,0,0,5,
        224,1,0,0,0,7,226,1,0,0,0,9,228,1,0,0,0,11,233,1,0,0,0,13,239,1,
        0,0,0,15,241,1,0,0,0,17,243,1,0,0,0,19,246,1,0,0,0,21,248,1,0,0,
        0,23,250,1,0,0,0,25,258,1,0,0,0,27,260,1,0,0,0,29,262,1,0,0,0,31,
        267,1,0,0,0,33,271,1,0,0,0,35,276,1,0,0,0,37,278,1,0,0,0,39,280,
        1,0,0,0,41,282,1,0,0,0,43,284,1,0,0,0,45,293,1,0,0,0,47,296,1,0,
        0,0,49,301,1,0,0,0,51,307,1,0,0,0,53,311,1,0,0,0,55,317,1,0,0,0,
        57,325,1,0,0,0,59,328,1,0,0,0,61,332,1,0,0,0,63,338,1,0,0,0,65,344,
        1,0,0,0,67,351,1,0,0,0,69,353,1,0,0,0,71,359,1,0,0,0,73,361,1,0,
        0,0,75,363,1,0,0,0,77,365,1,0,0,0,79,369,1,0,0,0,81,374,1,0,0,0,
        83,377,1,0,0,0,85,382,1,0,0,0,87,384,1,0,0,0,89,386,1,0,0,0,91,389,
        1,0,0,0,93,392,1,0,0,0,95,395,1,0,0,0,97,399,1,0,0,0,99,408,1,0,
        0,0,101,417,1,0,0,0,103,423,1,0,0,0,105,430,1,0,0,0,107,438,1,0,
        0,0,109,448,1,0,0,0,111,455,1,0,0,0,113,459,1,0,0,0,115,465,1,0,
        0,0,117,472,1,0,0,0,119,478,1,0,0,0,121,486,1,0,0,0,123,505,1,0,
        0,0,125,516,1,0,0,0,127,518,1,0,0,0,129,525,1,0,0,0,131,530,1,0,
        0,0,133,552,1,0,0,0,135,598,1,0,0,0,137,600,1,0,0,0,139,608,1,0,
        0,0,141,610,1,0,0,0,143,612,1,0,0,0,145,620,1,0,0,0,147,629,1,0,
        0,0,149,631,1,0,0,0,151,633,1,0,0,0,153,643,1,0,0,0,155,645,1,0,
        0,0,157,648,1,0,0,0,159,659,1,0,0,0,161,668,1,0,0,0,163,674,1,0,
        0,0,165,677,1,0,0,0,167,679,1,0,0,0,169,683,1,0,0,0,171,687,1,0,
        0,0,173,693,1,0,0,0,175,695,1,0,0,0,177,704,1,0,0,0,179,706,1,0,
        0,0,181,708,1,0,0,0,183,719,1,0,0,0,185,721,1,0,0,0,187,731,1,0,
        0,0,189,733,1,0,0,0,191,735,1,0,0,0,193,744,1,0,0,0,195,751,1,0,
        0,0,197,753,1,0,0,0,199,755,1,0,0,0,201,757,1,0,0,0,203,759,1,0,
        0,0,205,761,1,0,0,0,207,763,1,0,0,0,209,766,1,0,0,0,211,773,1,0,
        0,0,213,779,1,0,0,0,215,794,1,0,0,0,217,218,5,45,0,0,218,2,1,0,0,
        0,219,220,5,110,0,0,220,221,5,117,0,0,221,222,5,108,0,0,222,223,
        5,108,0,0,223,4,1,0,0,0,224,225,5,46,0,0,225,6,1,0,0,0,226,227,5,
        44,0,0,227,8,1,0,0,0,228,229,5,116,0,0,229,230,5,104,0,0,230,231,
        5,105,0,0,231,232,5,115,0,0,232,10,1,0,0,0,233,234,5,115,0,0,234,
        235,5,117,0,0,235,236,5,112,0,0,236,237,5,101,0,0,237,238,5,114,
        0,0,238,12,1,0,0,0,239,240,5,91,0,0,240,14,1,0,0,0,241,242,5,93,
        0,0,242,16,1,0,0,0,243,244,5,61,0,0,244,245,5,62,0,0,245,18,1,0,
        0,0,246,247,5,40,0,0,247,20,1,0,0,0,248,249,5,41,0,0,249,22,1,0,
        0,0,250,251,5,102,0,0,251,252,5,111,0,0,252,253,5,114,0,0,253,254,
        5,83,0,0,254,255,5,111,0,0,255,256,5,109,0,0,256,257,5,101,0,0,257,
        24,1,0,0,0,258,259,5,123,0,0,259,26,1,0,0,0,260,261,5,125,0,0,261,
        28,1,0,0,0,262,263,5,116,0,0,263,264,5,121,0,0,264,265,5,112,0,0,
        265,266,5,101,0,0,266,30,1,0,0,0,267,268,5,118,0,0,268,269,5,97,
        0,0,269,270,5,108,0,0,270,32,1,0,0,0,271,272,5,119,0,0,272,273,5,
        105,0,0,273,274,5,116,0,0,274,275,5,104,0,0,275,34,1,0,0,0,276,277,
        5,35,0,0,277,36,1,0,0,0,278,279,5,58,0,0,279,38,1,0,0,0,280,281,
        5,95,0,0,281,40,1,0,0,0,282,283,5,42,0,0,283,42,1,0,0,0,284,285,
        5,105,0,0,285,286,5,109,0,0,286,287,5,112,0,0,287,288,5,108,0,0,
        288,289,5,105,0,0,289,290,5,99,0,0,290,291,5,105,0,0,291,292,5,116,
        0,0,292,44,1,0,0,0,293,294,5,105,0,0,294,295,5,102,0,0,295,46,1,
        0,0,0,296,297,5,101,0,0,297,298,5,108,0,0,298,299,5,115,0,0,299,
        300,5,101,0,0,300,48,1,0,0,0,301,302,5,119,0,0,302,303,5,104,0,0,
        303,304,5,105,0,0,304,305,5,108,0,0,305,306,5,101,0,0,306,50,1,0,
        0,0,307,308,5,116,0,0,308,309,5,114,0,0,309,310,5,121,0,0,310,52,
        1,0,0,0,311,312,5,99,0,0,312,313,5,97,0,0,313,314,5,116,0,0,314,
        315,5,99,0,0,315,316,5,104,0,0,316,54,1,0,0,0,317,318,5,102,0,0,
        318,319,5,105,0,0,319,320,5,110,0,0,320,321,5,97,0,0,321,322,5,108,
        0,0,322,323,5,108,0,0,323,324,5,121,0,0,324,56,1,0,0,0,325,326,5,
        100,0,0,326,327,5,111,0,0,327,58,1,0,0,0,328,329,5,102,0,0,329,330,
        5,111,0,0,330,331,5,114,0,0,331,60,1,0,0,0,332,333,5,121,0,0,333,
        334,5,105,0,0,334,335,5,101,0,0,335,336,5,108,0,0,336,337,5,100,
        0,0,337,62,1,0,0,0,338,339,5,116,0,0,339,340,5,104,0,0,340,341,5,
        114,0,0,341,342,5,111,0,0,342,343,5,119,0,0,343,64,1,0,0,0,344,345,
        5,114,0,0,345,346,5,101,0,0,346,347,5,116,0,0,347,348,5,117,0,0,
        348,349,5,114,0,0,349,350,5,110,0,0,350,66,1,0,0,0,351,352,5,61,
        0,0,352,68,1,0,0,0,353,354,5,109,0,0,354,355,5,97,0,0,355,356,5,
        116,0,0,356,357,5,99,0,0,357,358,5,104,0,0,358,70,1,0,0,0,359,360,
        5,43,0,0,360,72,1,0,0,0,361,362,5,126,0,0,362,74,1,0,0,0,363,364,
        5,33,0,0,364,76,1,0,0,0,365,366,5,110,0,0,366,367,5,101,0,0,367,
        368,5,119,0,0,368,78,1,0,0,0,369,370,5,108,0,0,370,371,5,97,0,0,
        371,372,5,122,0,0,372,373,5,121,0,0,373,80,1,0,0,0,374,375,5,60,
        0,0,375,376,5,45,0,0,376,82,1,0,0,0,377,378,5,99,0,0,378,379,5,97,
        0,0,379,380,5,115,0,0,380,381,5,101,0,0,381,84,1,0,0,0,382,383,5,
        124,0,0,383,86,1,0,0,0,384,385,5,64,0,0,385,88,1,0,0,0,386,387,5,
        62,0,0,387,388,5,58,0,0,388,90,1,0,0,0,389,390,5,60,0,0,390,391,
        5,58,0,0,391,92,1,0,0,0,392,393,5,60,0,0,393,394,5,37,0,0,394,94,
        1,0,0,0,395,396,5,118,0,0,396,397,5,97,0,0,397,398,5,114,0,0,398,
        96,1,0,0,0,399,400,5,111,0,0,400,401,5,118,0,0,401,402,5,101,0,0,
        402,403,5,114,0,0,403,404,5,114,0,0,404,405,5,105,0,0,405,406,5,
        100,0,0,406,407,5,101,0,0,407,98,1,0,0,0,408,409,5,97,0,0,409,410,
        5,98,0,0,410,411,5,115,0,0,411,412,5,116,0,0,412,413,5,114,0,0,413,
        414,5,97,0,0,414,415,5,99,0,0,415,416,5,116,0,0,416,100,1,0,0,0,
        417,418,5,102,0,0,418,419,5,105,0,0,419,420,5,110,0,0,420,421,5,
        97,0,0,421,422,5,108,0,0,422,102,1,0,0,0,423,424,5,115,0,0,424,425,
        5,101,0,0,425,426,5,97,0,0,426,427,5,108,0,0,427,428,5,101,0,0,428,
        429,5,100,0,0,429,104,1,0,0,0,430,431,5,112,0,0,431,432,5,114,0,
        0,432,433,5,105,0,0,433,434,5,118,0,0,434,435,5,97,0,0,435,436,5,
        116,0,0,436,437,5,101,0,0,437,106,1,0,0,0,438,439,5,112,0,0,439,
        440,5,114,0,0,440,441,5,111,0,0,441,442,5,116,0,0,442,443,5,101,
        0,0,443,444,5,99,0,0,444,445,5,116,0,0,445,446,5,101,0,0,446,447,
        5,100,0,0,447,108,1,0,0,0,448,449,5,105,0,0,449,450,5,109,0,0,450,
        451,5,112,0,0,451,452,5,111,0,0,452,453,5,114,0,0,453,454,5,116,
        0,0,454,110,1,0,0,0,455,456,5,100,0,0,456,457,5,101,0,0,457,458,
        5,102,0,0,458,112,1,0,0,0,459,460,5,99,0,0,460,461,5,108,0,0,461,
        462,5,97,0,0,462,463,5,115,0,0,463,464,5,115,0,0,464,114,1,0,0,0,
        465,466,5,111,0,0,466,467,5,98,0,0,467,468,5,106,0,0,468,469,5,101,
        0,0,469,470,5,99,0,0,470,471,5,116,0,0,471,116,1,0,0,0,472,473,5,
        116,0,0,473,474,5,114,0,0,474,475,5,97,0,0,475,476,5,105,0,0,476,
        477,5,116,0,0,477,118,1,0,0,0,478,479,5,101,0,0,479,480,5,120,0,
        0,480,481,5,116,0,0,481,482,5,101,0,0,482,483,5,110,0,0,483,484,
        5,100,0,0,484,485,5,115,0,0,485,120,1,0,0,0,486,487,5,112,0,0,487,
        488,5,97,0,0,488,489,5,99,0,0,489,490,5,107,0,0,490,491,5,97,0,0,
        491,492,5,103,0,0,492,493,5,101,0,0,493,122,1,0,0,0,494,506,3,193,
        96,0,495,499,5,96,0,0,496,500,3,149,74,0,497,500,3,151,75,0,498,
        500,3,181,90,0,499,496,1,0,0,0,499,497,1,0,0,0,499,498,1,0,0,0,500,
        501,1,0,0,0,501,499,1,0,0,0,501,502,1,0,0,0,502,503,1,0,0,0,503,
        504,5,96,0,0,504,506,1,0,0,0,505,494,1,0,0,0,505,495,1,0,0,0,506,
        124,1,0,0,0,507,508,5,116,0,0,508,509,5,114,0,0,509,510,5,117,0,
        0,510,517,5,101,0,0,511,512,5,102,0,0,512,513,5,97,0,0,513,514,5,
        108,0,0,514,515,5,115,0,0,515,517,5,101,0,0,516,507,1,0,0,0,516,
        511,1,0,0,0,517,126,1,0,0,0,518,521,5,39,0,0,519,522,3,177,88,0,
        520,522,3,181,90,0,521,519,1,0,0,0,521,520,1,0,0,0,522,523,1,0,0,
        0,523,524,5,39,0,0,524,128,1,0,0,0,525,526,5,39,0,0,526,527,3,193,
        96,0,527,130,1,0,0,0,528,531,3,183,91,0,529,531,3,185,92,0,530,528,
        1,0,0,0,530,529,1,0,0,0,531,533,1,0,0,0,532,534,7,0,0,0,533,532,
        1,0,0,0,533,534,1,0,0,0,534,132,1,0,0,0,535,539,5,34,0,0,536,538,
        3,161,80,0,537,536,1,0,0,0,538,541,1,0,0,0,539,537,1,0,0,0,539,540,
        1,0,0,0,540,542,1,0,0,0,541,539,1,0,0,0,542,553,5,34,0,0,543,544,
        5,34,0,0,544,545,5,34,0,0,545,546,5,34,0,0,546,547,1,0,0,0,547,548,
        3,163,81,0,548,549,5,34,0,0,549,550,5,34,0,0,550,551,5,34,0,0,551,
        553,1,0,0,0,552,535,1,0,0,0,552,543,1,0,0,0,553,134,1,0,0,0,554,
        556,3,187,93,0,555,554,1,0,0,0,556,557,1,0,0,0,557,555,1,0,0,0,557,
        558,1,0,0,0,558,559,1,0,0,0,559,561,5,46,0,0,560,562,3,187,93,0,
        561,560,1,0,0,0,562,563,1,0,0,0,563,561,1,0,0,0,563,564,1,0,0,0,
        564,566,1,0,0,0,565,567,3,175,87,0,566,565,1,0,0,0,566,567,1,0,0,
        0,567,569,1,0,0,0,568,570,3,167,83,0,569,568,1,0,0,0,569,570,1,0,
        0,0,570,599,1,0,0,0,571,573,5,46,0,0,572,574,3,187,93,0,573,572,
        1,0,0,0,574,575,1,0,0,0,575,573,1,0,0,0,575,576,1,0,0,0,576,578,
        1,0,0,0,577,579,3,175,87,0,578,577,1,0,0,0,578,579,1,0,0,0,579,581,
        1,0,0,0,580,582,3,167,83,0,581,580,1,0,0,0,581,582,1,0,0,0,582,599,
        1,0,0,0,583,584,3,187,93,0,584,586,3,175,87,0,585,587,3,167,83,0,
        586,585,1,0,0,0,586,587,1,0,0,0,587,599,1,0,0,0,588,590,3,187,93,
        0,589,588,1,0,0,0,590,591,1,0,0,0,591,589,1,0,0,0,591,592,1,0,0,
        0,592,594,1,0,0,0,593,595,3,175,87,0,594,593,1,0,0,0,594,595,1,0,
        0,0,595,596,1,0,0,0,596,597,3,167,83,0,597,599,1,0,0,0,598,555,1,
        0,0,0,598,571,1,0,0,0,598,583,1,0,0,0,598,589,1,0,0,0,599,136,1,
        0,0,0,600,601,3,171,85,0,601,602,3,159,79,0,602,138,1,0,0,0,603,
        609,3,137,68,0,604,605,5,96,0,0,605,606,3,137,68,0,606,607,5,96,
        0,0,607,609,1,0,0,0,608,603,1,0,0,0,608,604,1,0,0,0,609,140,1,0,
        0,0,610,611,7,1,0,0,611,142,1,0,0,0,612,613,7,2,0,0,613,144,1,0,
        0,0,614,621,5,59,0,0,615,617,3,147,73,0,616,615,1,0,0,0,617,618,
        1,0,0,0,618,616,1,0,0,0,618,619,1,0,0,0,619,621,1,0,0,0,620,614,
        1,0,0,0,620,616,1,0,0,0,621,622,1,0,0,0,622,623,6,72,0,0,623,146,
        1,0,0,0,624,630,5,10,0,0,625,627,5,13,0,0,626,628,5,10,0,0,627,626,
        1,0,0,0,627,628,1,0,0,0,628,630,1,0,0,0,629,624,1,0,0,0,629,625,
        1,0,0,0,630,148,1,0,0,0,631,632,7,3,0,0,632,150,1,0,0,0,633,634,
        5,92,0,0,634,636,5,117,0,0,635,637,5,117,0,0,636,635,1,0,0,0,636,
        637,1,0,0,0,637,638,1,0,0,0,638,639,3,165,82,0,639,640,3,165,82,
        0,640,641,3,165,82,0,641,642,3,165,82,0,642,152,1,0,0,0,643,644,
        7,4,0,0,644,154,1,0,0,0,645,646,7,5,0,0,646,156,1,0,0,0,647,649,
        5,47,0,0,648,647,1,0,0,0,648,649,1,0,0,0,649,651,1,0,0,0,650,652,
        3,155,77,0,651,650,1,0,0,0,652,653,1,0,0,0,653,651,1,0,0,0,653,654,
        1,0,0,0,654,158,1,0,0,0,655,658,3,173,86,0,656,658,3,187,93,0,657,
        655,1,0,0,0,657,656,1,0,0,0,658,661,1,0,0,0,659,657,1,0,0,0,659,
        660,1,0,0,0,660,664,1,0,0,0,661,659,1,0,0,0,662,663,5,95,0,0,663,
        665,3,157,78,0,664,662,1,0,0,0,664,665,1,0,0,0,665,160,1,0,0,0,666,
        669,7,6,0,0,667,669,3,181,90,0,668,666,1,0,0,0,668,667,1,0,0,0,669,
        162,1,0,0,0,670,673,3,161,80,0,671,673,3,147,73,0,672,670,1,0,0,
        0,672,671,1,0,0,0,673,676,1,0,0,0,674,672,1,0,0,0,674,675,1,0,0,
        0,675,164,1,0,0,0,676,674,1,0,0,0,677,678,7,7,0,0,678,166,1,0,0,
        0,679,680,7,8,0,0,680,168,1,0,0,0,681,684,7,9,0,0,682,684,3,197,
        98,0,683,681,1,0,0,0,683,682,1,0,0,0,684,170,1,0,0,0,685,688,2,97,
        122,0,686,688,3,199,99,0,687,685,1,0,0,0,687,686,1,0,0,0,688,172,
        1,0,0,0,689,694,3,169,84,0,690,694,3,171,85,0,691,694,3,205,102,
        0,692,694,3,201,100,0,693,689,1,0,0,0,693,690,1,0,0,0,693,691,1,
        0,0,0,693,692,1,0,0,0,694,174,1,0,0,0,695,697,7,10,0,0,696,698,7,
        11,0,0,697,696,1,0,0,0,697,698,1,0,0,0,698,700,1,0,0,0,699,701,3,
        187,93,0,700,699,1,0,0,0,701,702,1,0,0,0,702,700,1,0,0,0,702,703,
        1,0,0,0,703,176,1,0,0,0,704,705,2,32,127,0,705,178,1,0,0,0,706,707,
        2,33,127,0,707,180,1,0,0,0,708,709,5,92,0,0,709,710,7,12,0,0,710,
        182,1,0,0,0,711,720,5,48,0,0,712,716,3,189,94,0,713,715,3,187,93,
        0,714,713,1,0,0,0,715,718,1,0,0,0,716,714,1,0,0,0,716,717,1,0,0,
        0,717,720,1,0,0,0,718,716,1,0,0,0,719,711,1,0,0,0,719,712,1,0,0,
        0,720,184,1,0,0,0,721,722,5,48,0,0,722,723,5,120,0,0,723,725,3,165,
        82,0,724,726,3,165,82,0,725,724,1,0,0,0,726,727,1,0,0,0,727,725,
        1,0,0,0,727,728,1,0,0,0,728,186,1,0,0,0,729,732,5,48,0,0,730,732,
        3,189,94,0,731,729,1,0,0,0,731,730,1,0,0,0,732,188,1,0,0,0,733,734,
        2,49,57,0,734,190,1,0,0,0,735,736,3,137,68,0,736,192,1,0,0,0,737,
        738,3,169,84,0,738,739,3,159,79,0,739,745,1,0,0,0,740,741,3,171,
        85,0,741,742,3,159,79,0,742,745,1,0,0,0,743,745,3,157,78,0,744,737,
        1,0,0,0,744,740,1,0,0,0,744,743,1,0,0,0,745,194,1,0,0,0,746,752,
        3,197,98,0,747,752,3,199,99,0,748,752,3,201,100,0,749,752,3,203,
        101,0,750,752,3,205,102,0,751,746,1,0,0,0,751,747,1,0,0,0,751,748,
        1,0,0,0,751,749,1,0,0,0,751,750,1,0,0,0,752,196,1,0,0,0,753,754,
        7,13,0,0,754,198,1,0,0,0,755,756,7,14,0,0,756,200,1,0,0,0,757,758,
        7,15,0,0,758,202,1,0,0,0,759,760,7,16,0,0,760,204,1,0,0,0,761,762,
        7,17,0,0,762,206,1,0,0,0,763,764,7,18,0,0,764,208,1,0,0,0,765,767,
        3,147,73,0,766,765,1,0,0,0,767,768,1,0,0,0,768,766,1,0,0,0,768,769,
        1,0,0,0,769,770,1,0,0,0,770,771,6,104,0,0,771,210,1,0,0,0,772,774,
        3,153,76,0,773,772,1,0,0,0,774,775,1,0,0,0,775,773,1,0,0,0,775,776,
        1,0,0,0,776,777,1,0,0,0,777,778,6,105,0,0,778,212,1,0,0,0,779,780,
        5,47,0,0,780,781,5,42,0,0,781,786,1,0,0,0,782,785,3,213,106,0,783,
        785,9,0,0,0,784,782,1,0,0,0,784,783,1,0,0,0,785,788,1,0,0,0,786,
        784,1,0,0,0,786,787,1,0,0,0,787,789,1,0,0,0,788,786,1,0,0,0,789,
        790,5,42,0,0,790,791,5,47,0,0,791,792,1,0,0,0,792,793,6,106,0,0,
        793,214,1,0,0,0,794,795,5,47,0,0,795,796,5,47,0,0,796,800,1,0,0,
        0,797,799,8,19,0,0,798,797,1,0,0,0,799,802,1,0,0,0,800,798,1,0,0,
        0,800,801,1,0,0,0,801,803,1,0,0,0,802,800,1,0,0,0,803,804,6,107,
        0,0,804,216,1,0,0,0,51,0,499,501,505,516,521,530,533,539,552,557,
        563,566,569,575,578,581,586,591,594,598,608,618,620,627,629,636,
        648,653,657,659,664,668,672,674,683,687,693,697,702,716,719,727,
        731,744,751,768,775,784,786,800,1,6,0,0
    ]

class ScalaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    T__50 = 51
    T__51 = 52
    T__52 = 53
    T__53 = 54
    T__54 = 55
    T__55 = 56
    T__56 = 57
    T__57 = 58
    T__58 = 59
    T__59 = 60
    T__60 = 61
    Id = 62
    BooleanLiteral = 63
    CharacterLiteral = 64
    SymbolLiteral = 65
    IntegerLiteral = 66
    StringLiteral = 67
    FloatingPointLiteral = 68
    Varid = 69
    BoundVarid = 70
    Paren = 71
    Delim = 72
    Semi = 73
    NL = 74
    NEWLINE = 75
    WS = 76
    COMMENT = 77
    LINE_COMMENT = 78

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'-'", "'null'", "'.'", "','", "'this'", "'super'", "'['", "']'", 
            "'=>'", "'('", "')'", "'forSome'", "'{'", "'}'", "'type'", "'val'", 
            "'with'", "'#'", "':'", "'_'", "'*'", "'implicit'", "'if'", 
            "'else'", "'while'", "'try'", "'catch'", "'finally'", "'do'", 
            "'for'", "'yield'", "'throw'", "'return'", "'='", "'match'", 
            "'+'", "'~'", "'!'", "'new'", "'lazy'", "'<-'", "'case'", "'|'", 
            "'@'", "'>:'", "'<:'", "'<%'", "'var'", "'override'", "'abstract'", 
            "'final'", "'sealed'", "'private'", "'protected'", "'import'", 
            "'def'", "'class'", "'object'", "'trait'", "'extends'", "'package'" ]

    symbolicNames = [ "<INVALID>",
            "Id", "BooleanLiteral", "CharacterLiteral", "SymbolLiteral", 
            "IntegerLiteral", "StringLiteral", "FloatingPointLiteral", "Varid", 
            "BoundVarid", "Paren", "Delim", "Semi", "NL", "NEWLINE", "WS", 
            "COMMENT", "LINE_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "T__44", "T__45", "T__46", "T__47", "T__48", "T__49", 
                  "T__50", "T__51", "T__52", "T__53", "T__54", "T__55", 
                  "T__56", "T__57", "T__58", "T__59", "T__60", "Id", "BooleanLiteral", 
                  "CharacterLiteral", "SymbolLiteral", "IntegerLiteral", 
                  "StringLiteral", "FloatingPointLiteral", "Varid", "BoundVarid", 
                  "Paren", "Delim", "Semi", "NL", "CharNoBackQuoteOrNewline", 
                  "UnicodeEscape", "WhiteSpace", "Opchar", "Op", "Idrest", 
                  "StringElement", "MultiLineChars", "HexDigit", "FloatType", 
                  "Upper", "Lower", "Letter", "ExponentPart", "PrintableChar", 
                  "PrintableCharExceptWhitespace", "CharEscapeSeq", "DecimalNumeral", 
                  "HexNumeral", "Digit", "NonZeroDigit", "VaridFragment", 
                  "Plainid", "UnicodeLetter", "UnicodeClass_LU", "UnicodeClass_LL", 
                  "UnicodeClass_LT", "UnicodeClass_LM", "UnicodeClass_LO", 
                  "UnicodeDigit", "NEWLINE", "WS", "COMMENT", "LINE_COMMENT" ]

    grammarFileName = "Scala.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


