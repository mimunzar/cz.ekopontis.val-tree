#!/usr/bin/env python3

import functools as ft

import src.val_tree.libs.util as util


TREE_OFFSET = {
    "abies sp."                                     : 268,
    "abies alba"                                    : 270,
    "abies alba 'pendula'"                          : 271,
    "abies alba 'pyramidalis'"                      : 272,
    "abies balsamea"                                : 269,
    "abies cephalonica"                             : 280,
    "abies concolor"                                : 279,
    "abies firma"                                   : 284,
    "abies grandis"                                 : 278,
    "abies holophylla"                              : 273,
    "abies homolepis"                               : 276,
    "abies koreana"                                 : 275,
    "abies lasiocarpa"                              : 282,
    "abies nordmanniana"                            : 274,
    "abies numidica"                                : 277,
    "abies pinsapo"                                 : 283,
    "abies procera"                                 : 286,
    "abies sibirica"                                : 281,
    "abies veitchii"                                : 285,
    "acer sp."                                      : 217,
    "acer campestre"                                : 218,
    "acer campestre 'elsrijk'"                      : 219,
    "acer campestre 'nanum'"                        : 220,
    "acer campestre 'postelense'"                   : 221,
    "acer campestre 'pulverulentum'"                : 222,
    "acer campestre 'queen elizabeth'"              : 223,
    "acer campestre 'red shine'"                    : 224,
    "acer campestre 'royal ruby'"                   : 225,
    "acer cappadocicum"                             : 239,
    "acer cappadocicum 'aureum'"                    : 240,
    "acer monspessulanum"                           : 232,
    "acer negundo"                                  : 233,
    "acer negundo 'aureo- variegatum'"              : 234,
    "acer negundo 'aureo-marginatum'"               : 235,
    "acer negundo 'flamingo'"                       : 236,
    "acer negundo 'odessanum'"                      : 237,
    "acer negundo 'variegatum'"                     : 238,
    "acer platanoides"                              : 249,
    "acer platanoides 'cleveland'"                  : 250,
    "acer platanoides 'columnare'"                  : 251,
    "acer platanoides 'crimson king'"               : 252,
    "acer platanoides 'crimson sentry'"             : 253,
    "acer platanoides 'deborah'"                    : 254,
    "acer platanoides 'drummondii'"                 : 255,
    "acer platanoides 'emerald queen'"              : 256,
    "acer platanoides 'faassen's black'"            : 257,
    "acer platanoides 'globosum'"                   : 258,
    "acer platanoides 'olmsted'"                    : 259,
    "acer platanoides 'palmatifidum'"               : 260,
    "acer platanoides 'royal red'"                  : 261,
    "acer platanoides 'schwedleri'"                 : 262,
    "acer platanoides 'summershade'"                : 263,
    "acer pseudoplatanus"                           : 241,
    "acer pseudoplatanus 'atropurpureum'"           : 242,
    "acer pseudoplatanus 'brilliantissimum'"        : 243,
    "acer pseudoplatanus 'erectum'"                 : 244,
    "acer pseudoplatanus 'leopoldii'"               : 245,
    "acer pseudoplatanus 'negenia'"                 : 246,
    "acer pseudoplatanus 'rotterdam'"               : 247,
    "acer pseudoplatanus 'worley'"                  : 248,
    "acer rubrum"                                   : 227,
    "acer rubrum 'armstrong'"                       : 228,
    "acer rubrum 'october glory'"                   : 229,
    "acer rubrum 'red sunset'"                      : 230,
    "acer rubrum 'scanlon'"                         : 231,
    "acer saccharinum"                              : 264,
    "acer saccharinum 'asplenifolium'"              : 265,
    "acer saccharinum 'laciniatum wieri'"           : 266,
    "acer saccharinum 'pyramidale'"                 : 267,
    "acer saccharum"                                : 226,
    "aesculus sp."                                  : 330,
    "aesculus flava"                                : 339,
    "aesculus hippocastanum"                        : 333,
    "aesculus hippocastanum 'baumannii'"            : 334,
    "aesculus hippocastanum 'fastigiata'"           : 335,
    "aesculus hippocastanum 'laciniata'"            : 336,
    "aesculus hippocastanum 'pyramidalis'"          : 337,
    "aesculus pavia"                                : 338,
    "aesculus x carnea"                             : 331,
    "aesculus x carnea 'briotii'"                   : 332,
    "ailanthus sp."                                 : 423,
    "ailanthus altissima"                           : 424,
    "alnus sp."                                     : 404,
    "alnus cordata"                                 : 410,
    "alnus glutinosa"                               : 405,
    "alnus glutinosa 'aurea'"                       : 406,
    "alnus glutinosa 'imperialis'"                  : 407,
    "alnus glutinosa 'laciniata'"                   : 408,
    "alnus incana"                                  : 411,
    "alnus incana 'aurea'"                          : 412,
    "alnus incana 'laciniata'"                      : 413,
    "alnus incana 'pendula'"                        : 414,
    "alnus x spaethii"                              : 409,
    "betula sp."                                    : 41,
    "betula alleghaniensis"                         : 58,
    "betula ermanii"                                : 50,
    "betula jacquemontii"                           : 51,
    "betula lenta"                                  : 57,
    "betula maximowicziana"                         : 52,
    "betula nigra"                                  : 49,
    "betula obscura"                                : 56,
    "betula oycoviensis"                            : 53,
    "betula papyrifera"                             : 54,
    "betula pendula"                                : 42,
    "betula pendula 'dalecarlica'"                  : 43,
    "betula pendula 'fastigiata'"                   : 44,
    "betula pendula 'laciniata'"                    : 45,
    "betula pendula 'purpurea'"                     : 46,
    "betula pendula 'tristis'"                      : 47,
    "betula pendula 'youngii'"                      : 48,
    "betula pubescens"                              : 55,
    "calocedrus sp."                                : 430,
    "calocedrus decurrens"                          : 431,
    "calocedrus decurrens 'aureovariegata'"         : 432,
    "carpinus sp."                                  : 162,
    "carpinus betulus"                              : 163,
    "carpinus betulus 'columnaris'"                 : 164,
    "carpinus betulus 'fastigiata'"                 : 165,
    "carpinus betulus 'frans fontaine'"             : 166,
    "carpinus betulus 'pendula'"                    : 167,
    "carpinus betulus 'purpurea'"                   : 168,
    "carpinus betulus 'quercifolia'"                : 169,
    "carya ovata"                                   : 415,
    "castanea sativa"                               : 340,
    "catalpa"                                       : 341,
    "catalpa bignonioides"                          : 344,
    "catalpa bignonioides 'nana'"                   : 345,
    "catalpa ovata"                                 : 346,
    "catalpa speciosa"                              : 343,
    "catalpa x erubescens"                          : 342,
    "cedrus sp."                                    : 88,
    "cedrus atlantica"                              : 89,
    "cedrus atlantica 'pendula'"                    : 90,
    "cedrus deodara"                                : 91,
    "cedrus libani"                                 : 92,
    "cedrus libani 'glauca'"                        : 93,
    "cedrus libani 'pendula'"                       : 94,
    "celtis sp."                                    : 38,
    "celtis australis"                              : 39,
    "celtis occidentalis"                           : 40,
    "cephalotaxus harringtonia"                     : 171,
    "cercidiphyllum sp."                            : 596,
    "cercidiphyllum japonicum"                      : 597,
    "cercidiphyllum japonicum 'pendulum'"           : 598,
    "corylus colurna"                               : 377,
    "crataegus sp."                                 : 172,
    "crataegus laevigata"                           : 174,
    "crataegus laevigata 'paul´s scarlet'"          : 175,
    "crataegus laevigata 'rubra plena'"             : 176,
    "crataegus monogyna"                            : 173,
    "cryptomeria sp."                               : 348,
    "cryptomeria japonica"                          : 349,
    "cryptomeria japonica 'araucarioides'"          : 350,
    "cryptomeria japonica 'cristata'"               : 351,
    "cunninghamia lanceolata"                       : 422,
    "davidia involucrata"                           : 128,
    "elaeagnus angustifolia"                        : 177,
    "fagus sp."                                     : 59,
    "fagus sylvatica"                               : 60,
    "fagus sylvatica 'ansorgei'"                    : 61,
    "fagus sylvatica 'aspleniifolia'"               : 62,
    "fagus sylvatica 'atropunicea'"                 : 63,
    "fagus sylvatica 'cochleata'"                   : 64,
    "fagus sylvatica 'cristata'"                    : 65,
    "fagus sylvatica 'dawyck gold'"                 : 66,
    "fagus sylvatica 'dawyck purple'"               : 67,
    "fagus sylvatica 'dawyck'"                      : 68,
    "fagus sylvatica 'laciniata'"                   : 69,
    "fagus sylvatica 'luteovariegata'"              : 70,
    "fagus sylvatica 'miltonensis'"                 : 71,
    "fagus sylvatica 'pendula'"                     : 72,
    "fagus sylvatica 'purple fountain'"             : 73,
    "fagus sylvatica 'purpurea nana'"               : 74,
    "fagus sylvatica 'purpurea pendula'"            : 75,
    "fagus sylvatica 'purpurea tricolor'"           : 76,
    "fagus sylvatica 'quercifolia'"                 : 77,
    "fagus sylvatica 'riversii'"                    : 78,
    "fagus sylvatica 'rohan gold'"                  : 79,
    "fagus sylvatica 'rohan obelisk'"               : 80,
    "fagus sylvatica 'rohanii'"                     : 81,
    "fagus sylvatica 'rotundifolia'"                : 82,
    "fagus sylvatica 'spaethiana'"                  : 83,
    "fagus sylvatica 'swat magret'"                 : 84,
    "fagus sylvatica 'tortuosa'"                    : 85,
    "fagus sylvatica 'tricolor'"                    : 86,
    "fagus sylvatica 'zlatia'"                      : 87,
    "fraxinus sp."                                  : 196,
    "fraxinus americana"                            : 197,
    "fraxinus angustifolia"                         : 201,
    "fraxinus angustifolia 'raywood'"               : 202,
    "fraxinus excelsior"                            : 203,
    "fraxinus excelsior 'allgold'"                  : 204,
    "fraxinus excelsior 'altena'"                   : 205,
    "fraxinus excelsior 'atlas'"                    : 206,
    "fraxinus excelsior 'aurea pendula'"            : 207,
    "fraxinus excelsior 'aurea'"                    : 208,
    "fraxinus excelsior 'crispa'"                   : 209,
    "fraxinus excelsior 'diversifolia'"             : 210,
    "fraxinus excelsior 'globosa'"                  : 211,
    "fraxinus excelsior 'heterophylla pendula'"     : 212,
    "fraxinus excelsior 'jaspidea'"                 : 213,
    "fraxinus excelsior 'nana'"                     : 214,
    "fraxinus excelsior 'pendula'"                  : 215,
    "fraxinus excelsior 'westhofs glorie'"          : 216,
    "fraxinus ornus"                                : 198,
    "fraxinus pennsylvanica"                        : 199,
    "fraxinus pennsylvanica 'aucubifolia'"          : 200,
    "ginkgo biloba"                                 : 324,
    "ginkgo biloba 'autumn gold'"                   : 325,
    "ginkgo biloba 'fastigiata'"                    : 326,
    "ginkgo biloba 'horizontalis'"                  : 327,
    "ginkgo biloba 'marieken'"                      : 328,
    "ginkgo biloba 'pendula'"                       : 329,
    "gleditsia sp."                                 : 133,
    "gleditsia triacanthos"                         : 134,
    "gleditsia triacanthos 'bujoti'"                : 135,
    "gleditsia triacanthos 'elegantissima'"         : 136,
    "gleditsia triacanthos 'shademaster'"           : 137,
    "gleditsia triacanthos 'skyline'"               : 138,
    "gleditsia triacanthos 'sunburst'"              : 139,
    "gleditsia triacanthos f. inermis"              : 140,
    "gymnocladus dioicus"                           : 403,
    "chamaecyparis sp."                             : 95,
    "chamaecyparis lawsoniana"                      : 103,
    "chamaecyparis lawsoniana 'alumii'"             : 104,
    "chamaecyparis lawsoniana 'columnaris'"         : 105,
    "chamaecyparis lawsoniana 'erecta viridis'"     : 106,
    "chamaecyparis lawsoniana 'filifera'"           : 107,
    "chamaecyparis lawsoniana 'fletcheri'"          : 108,
    "chamaecyparis lawsoniana 'glauca'"             : 109,
    "chamaecyparis lawsoniana 'golden wonder'"      : 110,
    "chamaecyparis lawsoniana 'ivonne'"             : 111,
    "chamaecyparis lawsoniana 'lane'"               : 112,
    "chamaecyparis lawsoniana 'lombartsii'"         : 113,
    "chamaecyparis lawsoniana 'lutescens'"          : 114,
    "chamaecyparis lawsoniana 'plumosa'"            : 115,
    "chamaecyparis lawsoniana 'silver queen'"       : 116,
    "chamaecyparis lawsoniana 'spek'"               : 117,
    "chamaecyparis lawsoniana 'stardust'"           : 118,
    "chamaecyparis lawsoniana 'stewartii'"          : 119,
    "chamaecyparis lawsoniana 'triomf van boskoop'" : 120,
    "chamaecyparis lawsoniana 'wisselii'"           : 121,
    "chamaecyparis nootkatensis"                    : 122,
    "chamaecyparis nootkatensis 'glauca'"           : 123,
    "chamaecyparis nootkatensis 'pendula'"          : 124,
    "chamaecyparis obtusa"                          : 125,
    "chamaecyparis pisifera"                        : 96,
    "chamaecyparis pisifera 'boulevard'"            : 97,
    "chamaecyparis pisifera 'filifera aurea'"       : 98,
    "chamaecyparis pisifera 'filifera'"             : 99,
    "chamaecyparis pisifera 'plumosa aurea'"        : 100,
    "chamaecyparis pisifera 'plumosa'"              : 101,
    "chamaecyparis pisifera 'squarrosa'"            : 102,
    "chamaecyparis thyoides"                        : 126,
    "juglans sp."                                   : 416,
    "juglans ailanthifolia"                         : 420,
    "juglans cinerea"                               : 419,
    "juglans mandshurica"                           : 418,
    "juglans nigra"                                 : 417,
    "juglans regia"                                 : 421,
    "juniperus sp."                                 : 189,
    "juniperus communis"                            : 190,
    "juniperus scopulorum"                          : 191,
    "juniperus scopulorum 'skyrocket'"              : 192,
    "juniperus virginiana"                          : 193,
    "juniperus virginiana 'glauca'"                 : 194,
    "juniperus virginiana 'kosteri'"                : 195,
    "koelreuteria paniculata"                       : 505,
    "koelreuteria paniculata 'fastigiata'"          : 506,
    "koelreuteria sp."                              : 504,
    "larix sp."                                     : 387,
    "larix decidua"                                 : 394,
    "larix decidua 'pendula'"                       : 395,
    "larix gmelini"                                 : 389,
    "larix kaempferi"                               : 390,
    "larix kaempferi 'blue rabbit'"                 : 391,
    "larix kaempferi 'diana'"                       : 392,
    "larix kaempferi 'pendula'"                     : 393,
    "larix laricina"                                : 388,
    "larix occidentalis"                            : 397,
    "larix sibirica"                                : 396,
    "liquidambar sp."                               : 1,
    "liquidambar styraciflua"                       : 2,
    "liriodendron"                                  : 352,
    "liriodendron tulipifera"                       : 353,
    "liriodendron tulipifera 'aureomarginatum'"     : 354,
    "liriodendron tulipifera 'fastigiatum'"         : 355,
    "maclura pomifera"                              : 437,
    "magnolia sp."                                  : 378,
    "magnolia acuminata"                            : 381,
    "magnolia hypoleuca"                            : 380,
    "magnolia kobus"                                : 379,
    "malus sp."                                     : 184,
    "malus domestica"                               : 185,
    "malus spectabilis"                             : 187,
    "malus sylvestris"                              : 186,
    "malus x zumi"                                  : 188,
    "metasequoia glyptostroboides"                  : 386,
    "morus sp."                                     : 399,
    "morus alba"                                    : 400,
    "morus alba 'pendula'"                          : 401,
    "morus nigra"                                   : 398,
    "ostrya carpinifolia"                           : 170,
    "padus sp."                                     : 498,
    "padus avium"                                   : 499,
    "padus avium 'albertii'"                        : 500,
    "parrotia persica"                              : 428,
    "paulownia tomentosa"                           : 429,
    "phellodendron amurense"                        : 347,
    "picea sp."                                     : 450,
    "picea abies"                                   : 485,
    "picea abies 'argenteospica'"                   : 486,
    "picea abies 'aurea magnifica'"                 : 487,
    "picea abies 'aurea'"                           : 488,
    "picea abies 'cincinnata'"                      : 489,
    "picea abies 'columnaris'"                      : 490,
    "picea abies 'cranstonii'"                      : 491,
    "picea abies 'cupressina'"                      : 492,
    "picea abies 'inversa'"                         : 493,
    "picea abies 'pendula major'"                   : 494,
    "picea abies 'rothenhaus'"                      : 495,
    "picea abies 'viminalis'"                       : 496,
    "picea abies 'virgata'"                         : 497,
    "picea alcoquiana"                              : 457,
    "picea asperata"                                : 456,
    "picea breweriana"                              : 452,
    "picea engelmannii"                             : 458,
    "picea glauca"                                  : 478,
    "picea jezoensis"                               : 451,
    "picea likiangensis"                            : 460,
    "picea mariana"                                 : 453,
    "picea mariana 'beissneri'"                     : 454,
    "picea omorika"                                 : 461,
    "picea omorika 'pendula'"                       : 462,
    "picea orientalis"                              : 479,
    "picea orientalis 'atrovirens'"                 : 480,
    "picea orientalis 'aurea'"                      : 481,
    "picea orientalis 'aureospica'"                 : 482,
    "picea orientalis 'gracilis'"                   : 483,
    "picea pungens"                                 : 463,
    "picea pungens 'edith'"                         : 464,
    "picea pungens 'endtz'"                         : 465,
    "picea pungens 'erich frahm'"                   : 466,
    "picea pungens 'fat albert'"                    : 467,
    "picea pungens 'fürst bismarck'"                : 468,
    "picea pungens 'glauca'"                        : 469,
    "picea pungens 'hoopsii'"                       : 470,
    "picea pungens 'koster'"                        : 471,
    "picea pungens 'moerheim'"                      : 472,
    "picea pungens 'montgomery'"                    : 473,
    "picea pungens 'oldenburg'"                     : 474,
    "picea pungens 'spek'"                          : 475,
    "picea rubens"                                  : 455,
    "picea schrenkiana"                             : 476,
    "picea sitchensis"                              : 477,
    "picea torano"                                  : 459,
    "picea wilsonii"                                : 484,
    "pinus sp."                                     : 3,
    "pinus aristata"                                : 23,
    "pinus banksiana"                               : 4,
    "pinus bungeana"                                : 7,
    "pinus cembra"                                  : 20,
    "pinus contorta"                                : 24,
    "pinus densiflora"                              : 14,
    "pinus flexilis"                                : 21,
    "pinus flexilis 'temple'"                       : 22,
    "pinus jeffreyi"                                : 15,
    "pinus koraiensis"                              : 16,
    "pinus leucodermis"                             : 5,
    "pinus nigra"                                   : 8,
    "pinus parviflora"                              : 9,
    "pinus parviflora 'glauca'"                     : 10,
    "pinus parviflora 'negishi'"                    : 11,
    "pinus parviflora 'tempelhof'"                  : 12,
    "pinus peuce"                                   : 26,
    "pinus ponderosa"                               : 28,
    "pinus pumila"                                  : 35,
    "pinus rigida"                                  : 30,
    "pinus rotundata"                               : 6,
    "pinus strobus"                                 : 31,
    "pinus strobus 'contorta'"                      : 32,
    "pinus strobus 'fastigiata'"                    : 33,
    "pinus strobus 'pendula'"                       : 34,
    "pinus sylvestris"                              : 17,
    "pinus sylvestris 'aurea'"                      : 18,
    "pinus sylvestris 'fastigiata'"                 : 19,
    "pinus thunbergii"                              : 29,
    "pinus uncinata"                                : 25,
    "pinus wallichiana"                             : 13,
    "pinus x schwerinii"                            : 27,
    "platanus sp."                                  : 433,
    "platanus occidentalis"                         : 436,
    "platanus orientalis"                           : 435,
    "platanus x hispanica"                          : 434,
    "populus sp."                                   : 517,
    "populus alba"                                  : 520,
    "populus alba 'nivea'"                          : 521,
    "populus alba 'pyramidalis'"                    : 522,
    "populus balsamifera"                           : 518,
    "populus lasiocarpa"                            : 526,
    "populus nigra"                                 : 523,
    "populus nigra 'italica'"                       : 524,
    "populus simonii"                               : 531,
    "populus simonii 'fastigiata'"                  : 532,
    "populus simonii 'pendula'"                     : 533,
    "populus tremula"                               : 528,
    "populus tremula 'erecta'"                      : 529,
    "populus tremula 'pendula'"                     : 530,
    "populus trichocarpa"                           : 525,
    "populus x berolinensis"                        : 519,
    "populus x canadensis"                          : 527,
    "populus x canescens"                           : 534,
    "prunus sp."                                    : 36,
    "prunus sp."                                    : 384,
    "prunus sp."                                    : 438,
    "prunus sp."                                    : 446,
    "prunus sp."                                    : 547,
    "prunus sp."                                    : 552,
    "prunus armeniaca"                              : 385,
    "prunus avium"                                  : 549,
    "prunus avium 'plena'"                          : 550,
    "prunus cerasifera"                             : 402,
    "prunus cerasus"                                : 561,
    "prunus domestica"                              : 447,
    "prunus domestica ssp. insititia"               : 449,
    "prunus hillieri 'spire'"                       : 548,
    "prunus kurilensis 'brillant'"                  : 448,
    "prunus mahaleb"                                : 382,
    "prunus padus 'colorata'"                       : 501,
    "prunus persica"                                : 37,
    "prunus sargentii"                              : 562,
    "prunus sargentii 'rancho'"                     : 563,
    "prunus serotina"                               : 502,
    "prunus serrula"                                : 551,
    "prunus serrulata"                              : 439,
    "prunus serrulata 'amanogawa'"                  : 440,
    "prunus serrulata 'kanzan'"                     : 441,
    "prunus serrulata 'kiku-shidare-sakura'"        : 442,
    "prunus serrulata 'ukon'"                       : 443,
    "prunus subhirtella"                            : 553,
    "prunus subhirtella 'autumnalis rosea'"         : 554,
    "prunus subhirtella 'autumnalis'"               : 555,
    "prunus subhirtella 'fukubana'"                 : 556,
    "prunus subhirtella 'pendula plena rosea'"      : 557,
    "prunus virginiana"                             : 503,
    "prunus x amygdalo-persica"                     : 383,
    "prunus x yedoensis"                            : 558,
    "prunus x yedoensis 'ivensii'"                  : 559,
    "prunus x yedoensis 'shidare yoshino'"          : 560,
    "pseudolarix amabilis"                          : 426,
    "pseudotsuga sp."                               : 129,
    "pseudotsuga menziesii"                         : 130,
    "pseudotsuga menziesii 'glauca pendula'"        : 131,
    "pseudotsuga menziesii var. glauca"             : 132,
    "pterocarya fraxinifolia"                       : 427,
    "pyrus sp."                                     : 178,
    "pyrus calleryana 'chanticleer'"                : 179,
    "pyrus calleryana 'redspire'"                   : 180,
    "pyrus communis"                                : 181,
    "pyrus communis 'beech hill'"                   : 182,
    "pyrus pyraster"                                : 183,
    "quercus sp."                                   : 141,
    "quercus alba"                                  : 143,
    "quercus cerris"                                : 145,
    "quercus coccinea"                              : 156,
    "quercus dalechampii"                           : 161,
    "quercus frainetto"                             : 158,
    "quercus imbricaria"                            : 144,
    "quercus macranthera"                           : 159,
    "quercus palustris"                             : 142,
    "quercus pedunculiflora"                        : 155,
    "quercus petraea"                               : 160,
    "quercus phellos"                               : 146,
    "quercus polycarpa"                             : 152,
    "quercus pubescens"                             : 153,
    "quercus robur"                                 : 149,
    "quercus robur 'fastigiata koster'"             : 150,
    "quercus robur 'fastigiata'"                    : 151,
    "quercus rubra"                                 : 147,
    "quercus virgiliana"                            : 148,
    "quercus x sargentii"                           : 154,
    "quercus x turneri 'pseudoturneri'"             : 157,
    "robinia sp."                                   : 537,
    "robinia luxurians"                             : 546,
    "robinia pseudoacacia"                          : 538,
    "robinia pseudoacacia 'bessoniana'"             : 539,
    "robinia pseudoacacia 'frisia'"                 : 540,
    "robinia pseudoacacia 'pyramidalis'"            : 541,
    "robinia pseudoacacia 'semperflorens'"          : 542,
    "robinia pseudoacacia 'tortuosa'"               : 543,
    "robinia pseudoacacia 'umbraculifera'"          : 544,
    "robinia viscosa"                               : 545,
    "salix sp."                                     : 564,
    "salix alba"                                    : 566,
    "salix alba 'liempde'"                          : 567,
    "salix alba 'sericea'"                          : 568,
    "salix alba ssp. vitellina"                     : 569,
    "salix babylonica"                              : 565,
    "salix caprea"                                  : 571,
    "salix daphnoides"                              : 573,
    "salix fragilis"                                : 572,
    "salix matsudana 'tortuosa'"                    : 570,
    "salix udensis"                                 : 576,
    "salix x rubens"                                : 574,
    "salix x sepulcralis"                           : 575,
    "sciadopitys verticillata"                      : 425,
    "sequoiadendron giganteum"                      : 444,
    "sequoiadendron giganteum 'pendula'"            : 445,
    "sophora sp."                                   : 293,
    "sophora japonica"                              : 294,
    "sophora japonica 'pendula'"                    : 295,
    "sophora japonica 'regent'"                     : 296,
    "sorbus sp."                                    : 297,
    "sorbus aria"                                   : 299,
    "sorbus aria 'aurea'"                           : 300,
    "sorbus aria 'lutescens'"                       : 301,
    "sorbus aria 'magnifica'"                       : 302,
    "sorbus aria 'majestica'"                       : 303,
    "sorbus aucuparia"                              : 306,
    "sorbus aucuparia 'edulis'"                     : 307,
    "sorbus aucuparia 'fastigiata'"                 : 308,
    "sorbus aucuparia 'pendula'"                    : 309,
    "sorbus aucuparia 'rossica major'"              : 310,
    "sorbus aucuparia 'sheerwater seedling'"        : 311,
    "sorbus domestica"                              : 304,
    "sorbus intermedia"                             : 305,
    "sorbus torminalis"                             : 298,
    "sorbus x hybrida"                              : 312,
    "taxodium sp."                                  : 510,
    "taxodium ascendens"                            : 516,
    "taxodium distichum"                            : 511,
    "taxodium distichum 'cascade falls'"            : 512,
    "taxodium distichum 'nutans'"                   : 513,
    "taxodium distichum 'pendens'"                  : 514,
    "taxodium distichum 'secrest'"                  : 515,
    "taxus sp."                                     : 507,
    "taxus baccata"                                 : 508,
    "taxus cuspidata"                               : 509,
    "thuja sp."                                     : 580,
    "thuja koraiensis"                              : 582,
    "thuja occidentalis"                            : 587,
    "thuja occidentalis 'alba'"                     : 588,
    "thuja occidentalis 'brabant'"                  : 589,
    "thuja occidentalis 'malonyana'"                : 590,
    "thuja occidentalis 'smaragd'"                  : 591,
    "thuja occidentalis 'spiralis'"                 : 592,
    "thuja occidentalis 'wareana'"                  : 593,
    "thuja orientalis"                              : 586,
    "thuja plicata"                                 : 583,
    "thuja plicata 'atrovirens'"                    : 584,
    "thuja plicata 'zebrina'"                       : 585,
    "thuja standishii"                              : 581,
    "thujopsis dolabrata"                           : 594,
    "thujopsis dolabrata 'variegata'"               : 595,
    "tilia sp."                                     : 356,
    "tilia americana"                               : 357,
    "tilia americana 'nova'"                        : 358,
    "tilia americana 'redmond'"                     : 359,
    "tilia cordata"                                 : 364,
    "tilia cordata 'green globe'"                   : 365,
    "tilia cordata 'greenspire'"                    : 366,
    "tilia cordata 'rancho'"                        : 367,
    "tilia cordata 'roelvo'"                        : 368,
    "tilia cordata 'winter orange'"                 : 369,
    "tilia petiolaris"                              : 363,
    "tilia platyphyllos"                            : 372,
    "tilia platyphyllos 'laciniata'"                : 373,
    "tilia platyphyllos 'örebro'"                   : 374,
    "tilia platyphyllos 'rubra'"                    : 375,
    "tilia tomentosa"                               : 370,
    "tilia tomentosa 'brabant'"                     : 371,
    "tilia x euchlora"                              : 376,
    "tilia x vulgaris"                              : 360,
    "tilia x vulgaris 'pallida'"                    : 361,
    "tilia x vulgaris 'zwarte linde'"               : 362,
    "torreya californica"                           : 535,
    "torreya nucifera"                              : 536,
    "tsuga sp."                                     : 287,
    "tsuga canadensis"                              : 289,
    "tsuga diversifolia"                            : 288,
    "tsuga heterophylla"                            : 291,
    "tsuga mertensiana"                             : 290,
    "tsuga sieboldii"                               : 292,
    "ulmus sp."                                     : 313,
    "ulmus glabra"                                  : 319,
    "ulmus glabra 'camperdownii'"                   : 320,
    "ulmus glabra 'exoniensis'"                     : 321,
    "ulmus glabra 'pendula'"                        : 322,
    "ulmus laevis"                                  : 323,
    "ulmus minor"                                   : 316,
    "ulmus minor 'dampieri aurea'"                  : 317,
    "ulmus parvifolia"                              : 314,
    "ulmus parvifolia 'geisha'"                     : 315,
    "ulmus x hollandica"                            : 318,
    "x cupressocyparis leylandii"                   : 127,
    "zelkova sp."                                   : 577,
    "zelkova carpinifolia"                          : 578,
    "zelkova serrata"                               : 579,
}

GROWTH_CONDITIONS = {
    1: "unaffected",
    2: "good",
    3: "impaired",
    4: "extreme",
}

def growth_conditions(v):
    return GROWTH_CONDITIONS[int(v)]


LOCATION_ATTRACTIVENESS = {
    1: "high",
    2: "medium",
    3: "less_significant",
    4: "low",
    5: "very_low",
}

def loc_attractiveness(v):
    return LOCATION_ATTRACTIVENESS[int(v)]


def optional_apply(f, x):
    return x if None == x else f(x)


def iter_trunk_diameter(x):
    return map(int, filter(util.identity, str(x).replace(',', ';').split(';')))


HABITAT_KEYS = [
    'rozštípnuté dřevo a trhliny (A/R)',
    'dutiny (A/R)',
    'suché větve (A/R)',
    'poškození borky (A)',
    'výtok mízy (A)',
    'zlomené větve (A)',
    'dutinky (A)',
    'plodnice hub (A)',
]


def iter_habitats(keys_it, tags_it, Measurement):
    h_it = zip(keys_it, util.pluck(keys_it, Measurement) or [])
    return map(util.first, filter(lambda x: util.second(x) in tags_it, h_it))


iter_microhabitats     = ft.partial(iter_habitats, HABITAT_KEYS, ['a', 'A'])
iter_ext_microhabitats = ft.partial(iter_habitats, HABITAT_KEYS, ['r', 'R'])
HABITAT_CODE = {
    'dutinky (A)'                       : 'a',
    'dutiny (A/R)'                      : 'b',
    'rozštípnuté dřevo a trhliny (A/R)' : 'i',
    'poškození borky (A)'               : 'h',
    'suché větve (A/R)'                 : 'j',
    'výtok mízy (A)'                    : 'm',
    'zlomené větve (A)'                 : 'f',
    'plodnice hub (A)'                  : 'g',
}

def habitat_code(h):
    return HABITAT_CODE[h]


def iter_names(names):
    return map(lambda s: s.strip(), names.split(r'|'))


def from_measurement(Measurement):
    cz, lat = iter_names(Measurement['Český název | Latinský název'])
    return {
        'taxon_offset'            : TREE_OFFSET[lat.lower()],
        'taxon'                   : f'{cz} ({lat})',
        '_taxon_cz'               : cz,
        '_taxon_lat'              : lat,
        'diameters'               : tuple(iter_trunk_diameter(Measurement['průměr kmene [cm]'])),
        'diameters_on_stumps'     : [],
        'height'                  : optional_apply(float, Measurement['výška stromu [m]']),
        'stem_height'             : optional_apply(float, Measurement['výška nasazení koruny [m]']),
        'spread'                  : None,
        'vitality'                : optional_apply(str, Measurement['vitalita']),
        'health'                  : optional_apply(str, Measurement['zdravotní stav']),
        'removed_crown_volume'    : optional_apply(int, Measurement['odstraněná část koruny [%]']),
        'location_attractiveness' : optional_apply(loc_attractiveness, Measurement['atraktivita umístění']),
        'growth_conditions'       : optional_apply(growth_conditions,  Measurement['růstové podmínky']),
        'microhabitats'           : tuple(map(habitat_code, iter_microhabitats(Measurement))),
        'extensive_microhabitats' : tuple(map(habitat_code, iter_ext_microhabitats(Measurement))),
        'memorial_tree'           : optional_apply(bool, Measurement['Památný strom (A)']),
        'deliberately_planted'    : False,
    }

