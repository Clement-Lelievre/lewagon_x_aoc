# following challenge 2017 day 9, I'm interested in checking the run time of two algorithms
import re
import time

INPUT = "{{{{{}},{{<!!!>>,{<!>},<!>},<<a>}},{{},{}},{{{<}>}},{{{<e},!!!>,io!!!>!>},<!>},<!!!>},<9!!>},{}}},{<ee!!!><>,{<,}}<<!!,<{,!!}ie!>>}}}},{{<a!>},<!!!!!>},<!!!!!>!!!ae99!e>,<eu9{!!!>!!}!,!!!>!>},<a!>},<i9!!!o>},{{<!!!>!o!>,<e!!{9{9,9!!u}a!!!!!>},<!>},<9>,<!>,<{<oai,9e>},{{},{<9!>,<9!>},<!!ai<!!!!!>},<,{e!>,<>}},{{{},{<e9a<!!u!!!>!u>}},{<a9ie!!{e9!>,,!>>},{{<!!!!}!>},<!>,<}9{!!o99u!9!!>,{<au!>!>,<99oa,!>>}},{{{<!!{!>},<{u!e{i!>,<{!!9a}!>,<<!>},<>}},<!!!!<!!!>}}u{!!!>>},{<!>},<}!>},<!>9!!,u>}}}},{{{<{<9!>},<!>},<!!!>!!9oi!>},<>},{<{{!!!}}{!>,<!!!!!!!>!!!>!!!>!>},<}!!}>,{}}},{{{<9,!>,<!!>},<{{>},{{{<!!!>o{>},<u!!!>},<!>},<9!>,<!>},<,e!,9!<!!!><<i9>},{{<!>,<}o!!!!}9!!!>a!!!!!><9,9}>}}},{{{{<e!!!>!!!>!!!>!>,<!!!>},<!>!!!>>}},{<!!!!!>!>,<eaoi}{!!!>a<,>,{<ei{,o!a9ee!>},<a9!<9u!uo>}}},{{<9i}!{e<!!}9u!!!>},<9}!!a>,<!>!>}}>}}}}}}},{{{{<!>},<!!!>,<}!!!>e}}i!io!!!!!>}ia>,{<>}},{{<!>o!{9!>,<!>,<u}{!>},<>},<o<u!>,<!>{a!!!>o!>,<!>},<99>}},{{{{<!>},<!{!>9!!!!{,ai9u!!!!a9i9o>,<!>},<!!!>o9e!>,a<!eu}ii9{>}},{{<o!>!<!!!>,<!!9}!{!>},<!>,<!!i<9!!9>}}},{{<,a!!!>e},u9u{!!!>>},<e!>}{!!u!>!!9>}},{{<!!i!,!!<}!!{!!a9>},{{<i!9!!!>9>}},{<!!9!!!>!!oi!<!!{!>{a<<!>,>}}},{{{{{<9<o!>},<{ui!!>},{}}},{<o!>>,<!>,<>}},{{{{{<!>9,!>!!!>!!!>!ia,>,<>},{<uo!!e!>,<u>}},{{<ia!>,<!a!>!>,<,ueu!><o!!<!!o!>>}}},{{{<!>},<{!!ee9!!iee>},<,i!!!>u!>},<}!>,<9uo!9u!>,<!!!!9>}},{{},{{}},{<,9>}}},{{<!{!a9iuiei{{ie!{{!>,<>}}},{{{},{{{}},{{<!!!!!>u!>,<!!!>9o!!!>9{!>},<}9!>,<!>,<!!!>9>}},{{<!!!!!>!>,<<!>},<!!!!a!!i!!i!!9!>},<!!u9>,{<!!ae9!!<!},aii}u>}},{<!!<,!>},<9,!>9u!>,<!!u9>}}},{{},{<}a!!!!ioi!<!!>}}},{{},<!>,<!}o9}i!!!>e!!!>iu!!<>}},{{<}!,{!o}9!>!{!>},<!>},<a,!!9!!!>,<<>,{<e!!9o!!i!>},<!>,<}},<,9ai!!!!!<uo>}},{{{{{<{u9!>},<>,{}}},{{<<aa!>},<!>,<!!!!!>},<!}e}!>},<!>,<9{!>>}},{{<!!!>},<!!!>ia!>,<{i>,{{<e,!>o>}}}}}},{<!!!>!!ai}{!>,<e9a!>},<>}},{{}}}},{{{{}},{{{<oe{9ooe!>,<!>},<!!9!!!>!!!!!!9!!!!!>,<}>}},{{<!!!>!!!!!>},<!!!!!>!!{{ae,!!e9>,{{<9ao{>}}}},{{<iiueo>},<}}o!!i>}},{{<{i<<!!!>!!a>,{{<ee{o!!!e,{,>}}},{<!>},<}a,i{i!!!}{!<!>,<>,{<!>u9!>,<,!!!>9!!o>}},{{<e!>},<ei!>,<!!!>!>,<oi>},<ii!!!>9!u9u<!!,!>,<!9!!!}!>,<!!!>!>},<i}>}}}},{{},{<}ea!>u,!>!!}e999!!!>,<!!a!>},<!!!!i>}}},{{{{<!>9!!!>{!>},<99!!!><o!!!>>}},{{{{<!!!!!>!>},<u!!!>>,{<!>!!{>}},{<9!!!>a!!!!ea!!oou9!u!>},<>,{}}},<!><!!!>u!!,!!!!!>>},{{{<!>}}!!!>},<!>,<}9!o!>,<9!>9!}o!!i9i9>},{<!>9a{!,9i!!!>a}o{e9u!>aiu>,{<}<a!!<>}}},{<!>},<a!!{!!!!!>!>},<i}!!!>oi!>!ea!>,<!>,<!>},<9>}}},{{<,e}o!!<i{!!<!a!!!>!!i!>>},{}}},{{},{<a<u!>,<!!!!!{i!!e!!!>!>,<>}},{{{}},{{<<!>},<9>},{{}}}},{{{<,!!!>},<!!!,oo,>}},{<!{o!><!e>,{}},{<9!>e!!!>u!>,<{!!!>!>,<o!}eo<!!{>}}},{{{{{}}},{{{{}}},{{<!9o!o!!!>!!oe9!i>},{<!>,,ea!a!>},<e!!,9!,!!!>,<!!!>!<!!>}},{<<o!>,<9<!!!>!>},<<!!o!!9>}},{{{},<!>,<u!!9<!!!>},<!!!>a9u{!>>},{{<!!ai9!>},<!o<e,,!!!!!<!!!!u!!e!>!>},<{!>,<>,{<e9<i!>},<>}},{{<<uiu!!i,9!>,<a!!o!>},<9}!!}9i!!<a>}},{<9>,{<!!oaoi{>}}},{{{{<,euia!e9>}}},{<!!!>!!}!!o9a!!!>!>}io!>o<!!!>,<,i<>,<!!!!!!!a>},{<ou!!u!>i9>,<!!}}u<{,!!i!>,<}!}>}}}},{{{{{{{{},{{{<!{e{,oi>}},{{<!!!<<!>,<o>}},{<!>,<{9e!>,<9u!e!>!!!>9!oa!!9!!u>,{<9!!!>a!>!>,ea!!!!,9}ii!>},<>}}}},{<>,<9>},{{{<!>,<!><9i>},{<,{e!{!o!!!>>}},{{<i9!!!>,<e!>{!>},<!{!!i,oeu<999>},{}},{}}},{{<9!>,<!9e!!9!!!>!>},<!!,>},{<i!>!>!}<!!o!!<!!!{!9!!!>!!!>!>,<<<!!!!>,{{<9!>,<u!>i!!i!e9!!!>!>!>,<!>},<!!,9<!9>}}}},{{<,!{!>,<!!u!!!!!>ue9a>},<a!9i!!!!!{ae9!!!>!!9999o!>,<9!u>}},{{<!!9,!!>,{{<!>,<!>!>,<99!aoa>}}},{{<i<!>},<u9ou!!},!!!>!!9!!>}},{<}!>},<!>a99e!!!>ui!>},<e}!!<!>a{>,{}}},{{<a9!>},<<!>,<o!>},<!!o9!!!!!!!>9!<!!!9i}9>,{}},{{{{<{!o!!!><,o{!>ueuoi!!!>{!!!!}!>},<>},<eoo!>!,iii!ui!>,<!>},<!>i9,,!!!>,<>},<!u{i}<!>,<u!>!>},<!>!!ai!u!!ia!!u!>},<>},{<aaou>}},{<!!!!!>},<,!!e<e!!!>i!>},<o9,o!!!>},<9>,<!<!!,!e9<u!>},<!>!!,!>},<!o>}}},{{{{{<!!!>oi>},<ui!>,<,!!o<!a},!>,<9ou!>,<!9<a{>},{{{<!!!>},<e,!>e{!!{9>},{}},{<9e!!9!>,<!>,<<>,<!!!>!>!}!>,<}i!>,<,!,>},{<!!!!o}{!!!>!!u{!>},<!!!!!!!!{iu!!!!!!!>,<,!!>,{}}}}}},{{{{<o!!}!!e!><!>,<!>},<}e>,<!>!!!>!>e!!99!!!>u!!9!u>}},{{<9!>>},{<!!!!!>a!>},<!!!>e!!!>!>},<!u{!u!>},<u!>,<>}}},{{{<>},{{<!>},<!>},<!>i}!!!>,<9uu!o!!{}{!!!>,<o!!!>>,<}e>}}},{{<io!!!9{!!9i!!!>9e9}a!>u!!!!ui!>},<>,<ao!a!uo!>,<!!!!,i,,u!>},<>},{{<o!!!>u9!9e!>,<!>,<!>},<!9u!!}!>,},e>},<a{9!>,<9a}!!!>!>,<o!!!>!a!>,<u!!i!}!>},<u9>},{{<!e!,u!>},<!>,<{a!>,<!!!!!{!u!>,<9!>,<!!9!>,<!!!<>},{<99!>},<>}}},{{{<!!{{>}},{{<9!a,9!!!>{!>},<!>},<!>},<!!!>!!},e!e>},{{},<!>},<!!!!a!9uau!!!!9o>}},{{<!!{,>},<{u!!!!!>>}}}},{{{{{<9!a!!!>!>},<o9!>o>,{{},<{!!!>!!a!!}!!e!!ai>}},{<eeuue>},{{<>,<!!!>ao!>a<,a,aie!>},<!>!>},<e!!>},{},{{<!>eoiu!>},<>,{{<{!!!>!!!!!!!>u!!!>!>},<!!!>>},<},9!>u!9ao>}}}}},{<!>},<9!>},<!a!>,<9}ui!>,<<!!!!,!!<a9!!e>},{<}o!,,!>!>},<>,{}}},{{},{{{<{!!!>o!>ii!!{ou{<!!9!!!>9>},{{},{<!>},<u>}}},{{<!!!>oe!>,<>}}},{<>}},{{{<!!!9o!>,,9!>},<9{u{!!!>},<!!!>!9!!!>>},{<!!{,>}},{{<<o!!!>!!!>i!!!>9!!,!!!!{!!!>!!!!!>{!>,<o!!!>>},<<<e!!!!!!!>!!9,eu9e}}!>!>},<>},{<!oa!>oa}!au!!9{!!!!!>9{!>,<}!>},<!!!!!>>}}}},{{{{},{{},{<,!!!>!>,<>,<!,,u9!>a9!>{i>},{{},{{{<!!a}i<}!>,<u!eo{!!,ui9,>}},{<!!!>ae,{!>e!!!!!>>}}}},{{<{!!!!!>i!!!!!a>,{<!!!>},<!>,<!!!>}!!!>,>}},{},{{<e<{!!9{!>,<a9!>},<<!ie999>,{}},{<!9!e}!!!>},<,oeuo!>!!!!!!!e>},{{<u!>,<!!!>>},{<!>,<u!!e!!e9>}}}}}},{{{<>},<uau>},{},{{{}},<a!>,<{a9!}!!!>!!!>9eu!!!>eii<{e>}},{{{<!!99!}i!9u!>{o9!>,<>},<a!>!!9}u9!>,<!>,<!>},<9!!!>},<<!o!!i>},{{},{{<!!!>i!!!!,{>},{<,u99i!><>}}},{}}}},{{{{{{<u}!!<o{!u!!u>}},{<9,<!!!>}e>,{<!>ao!>i9a{!>!>},<ou!!<!!,!9u}!>},<>}},{{{<ui>}},{}}},{{<!>,<!>,<a!>,<}!>},<i!>,<e>,{}},{},{<o!!,>,{<9!!i,!!!>ae9>}}}},{{{{<9e!!!>9u!!!!!>},<!!i>},{<!!!>},<u{,!>},<!!!!ia{!>,<!>},<{>}}},{{}}}}}},{{{{}},{<>},{{{<!>,<e!!!>>},{<!!!!!>,>}},{}}},{{}},{{},{<9o!>,<!!!!9!!!>i!i>,{<!>,<<<>}},{{{}}}},{{{{{},<{!!e!!!!!!!!{a!!!!e<!>ie,e!>},<o9!!!!>},{<i9e>,<!!!!{!!9!>,9iu!>},<o!a!!>},{<u!<!u!>!!!>},<}!>},<!>>,<uu!,>}},{{<!>,<,!!!>!!!>!!!>},<!!!>a!>,<>},{{{<i!>!i>}},{<!!!!!>99aa!>},<!e}!!!}o}>}}}}}},{{{{}},{{<!>},<a9!>},<<a!u9u{!!!>,<!>,<!>},<}<9>},{{<e!!9!}!>},<,!o!!oeoa>},{<u>,{{<a9<!99}!!!>!!e99!!>}}}}},{<{!o!>,<!>,<i!>},<i}u<io!!!!!>,<9{!>,>,{{<!!!!!!!!!>>}}}},{{}},{{{<}9!!a{!!9!>},<!!<9i!aiua!!9{>,{{<,!!e!!a!!,e!!oua<<i!!!>!o<a9!>,<>}}},{{},{<!>},<9}}9a!>,<i!!!>,<a!!!!!>99}o>}}},{}},{{{<!!e,!!!>9!{o!>,<!!i,!>,<!!io}>,<<!>},<!>>},{<!!9eo}<!>},<}!!!>},<9!99e<!>},<,u!>},<!>},<>,{{<!>,<{!>,<!!!><{o{ieu>}}}},{{{<{!!!!!}{9a!!uu9!u!!aa!!!o!!!>!>,<9>,<!>},<!!!>}{!!9>},{{<!>},<!>,<!>!>,<u!o{>,{}},{}},{{<!!<<u!!!,ie!>},<!!!>9>},<e9!!<a9}u{{!>9!>},<a!e!>,<!>{e>}},{{{<i!>},<!!!>,<9o!!!>},<!!oa!>e!!9,eu>},{<}!!!!!>{}{i999!!o9},<!!!>>}},{{<<ou!!{!!9!>},<9a!>},<!>,!>},<!!!>!<!!!>},<>},<99{a!>},<{9ia!>e!>,<>},{}}},{{{<!!!>},<<o,u>,{<!>},<9!>,<9au>}},{{<!>},<i!>},<{!>,<u!o>},{<u!<,!>{u<<!!!ia>}},{{{<!!!!!>a<!!o!>},<e},}{e9u{u}>}}}},{{{<!!!>,ueiu!!>}},{{<9o!>a>},{{<iu!!>},{{{<!>,<u!!!!,,ei!>,<u>}}}}},{{{}},{{<!!!>9u<iau!>},<a!!!!oe>}}}},{}},{{<!!!>e!>},<!{{}!!!!!u9o{u!!9!<{e>,{}},{<{i!!!>,<!!!>>},{<iiu>}}}},{{{{{{{<e!!!>},<!!u,i!!!e!>}!i!!!>>,{<a!>,<a9!!9!e!!!>!>,<e!>},<9!>},<!ia{!>,<9>}},{{<!!{e,!>},<ee!!!<<99!!aao!>,<!}<!!e}>},{<!>,<!>},<,!!!>!<!>>}}},{{}},{},{{{},{<{>}},{{},<!>!>,,!>},<i}!!}!!!>{!!!>e>}}},{{{{{<,ei!>,<!!!>},<9!!>},{<,e!!!ua<a!!!!!>9!>ia!!<}{!!!>},<!9>,{}},{{<!!!>!>,<a9!>},<<!!!>9e!!e9!!!>!>!>ea>,{}},<!>9o>}}},{{{<>},{<oe!<!!!!ie!!,!!!!!>!oa!>,<{}!!!>,>}},{<>},{}},{<!>},<!uu>,{}}}},{{{},{<!!!!!>u,99!!!!!>},}}!!<{u9!,{>}},{{{{<!>i}a!>,<!,,!>oa!>,<u>}}},<u!>}{i9a>}}},{{<o!!!>!>!!i{9,!!}>,{<!!,,<!!!>a!>},<}!<!o<{>,{<a!!{e!,o>}}},{<,!!i!!9io!>,<!!!>!!!><i!uiu!>},<>,{{{}},<i}i}9>}},{{<99!!,i!!!>{}!!<uo9e>}}}},{{{{<!>,<<{!>,<!!<>},<o9e!!!!!!!>o!!>},{<!,!!,!>,<!>{!>,<,o}{o!>,<!oa!i9>},{<!>},<<!>,<}e<>}},{{<9iei!i<!!!>o,!>,<99!!!>a!!!>{!>,<e<>},<o>},{}}},{{{<!>e!>},<uiei!!>},{{{<!!{>},{<>}}}},{{{{<<i!>,<u>}}},{{{<}!!!>!>,<a9!!!>!!!!}9a!!!!!!!!!><}!>,<uo>},<!o}!!!>a9!!,!>{>},{<a!>},<u!!!>9uu!!{9}9!a{!!u!!!>},<9>,{<!>,<>}}},{{<}>,<!>,<o!>9!!!>!9>}}}}}},{{{{}},{{<!a9,9>},{}},{{{{<!!ee!>,<!!ue!>,<uu>}},<!!!<u999uu,!!<!>},<!>o!>>},{}}},{{},{<>},{{<!!{o<!!!!!}au9>},<!!!,,<!!u9!>},<u!>9!!!>9<<!!!!ui!>,<>}}},{{{<9,o9}!>,<}!!!>!au>},{{<o!<!!!>,<ie{!!{9eu!!!>!>i{>},<!>},<!!!!!>!>9<!>},<9ie,!>!!!>>}},{{{},{{{<!!9e!ae9!>!!!>oo!>,<9>},<!>9{<>}},{<9>,{{<a9e>}}}},{<{!!,>},{<{!!}!>},<!!9ii{!9!!!><!>,<!>,<!!!!!>>,<!!!>!<ee}u!!!i!uei>}},{{}},{{{{<!!!i}9!9>,{<<{u99!!a!>,<>}},{{<!u,!,{9e<oo!>>}}},{{<oo!!u!!e99!i!>>},{{<ai!>,<9!>},<{!>}!>},<>},<!>,<a<>}},{<i!>},<!>},<!!!>},<,<!9{9>,{<9!e9!>,<!!!>!>,<>}}},{{{<!>,<!!>}},{}},{{<!!!!!>i!>,<i,u!>},<u!!e!>,<99!>},<{9!>!>},<>},<!9{!9<<!>,<{!{9o>}}}}},{{{{{<!>!>a!!}i!>,<!!u!!{!>},<>},{}},{{<9!>9{!!9!!{!!!>!!9!<!<!!!!!>},<>,{{<i!u!>,<9>}}}},{{<,<a!u!!!>,!<i!>,<!i,>},<!>o!!o!u>}},{{{<9,9!!!>,<!>,<9>},{{{<>}},{}},{{{{<!!<!!,oi>},<!!<>},{{{}},{<!i!9}a!>},<o9a>,{<9<9e!!!!{>}}}},{<!>},<!>},<}!i!!9,,!!!>}!9!!!>,<!!!>>,<!>,<eu!>},<!o!!!,<<<!!!>>},{{{{},<,u!>},<i!!!!!>},<e>}},{{{}},{{<!>,<!!!><!e!{u!!e{<<,}!>,<{!>!!}!!9>}}},{{{{<!>aa!!!>}!!!>o,9!>},<}!!}!ie!>,<9!!!>i!!>}},{<9!>9o!>},<!9}a!!!>!>,<!9e<!!{!>,<!!}9>}}}}}},{},{{{{{{<!!!!9>}},{<!>,<{i!>,<!>},<o9oi!9}>}},{{<!!!><{u>},<!>},<!!!>!!!9!!i9u}!u>},{{}}},{{<o<,!!!>ou!!!>,<uee{9!><<9>},{<e<o<,,!!!!!!<<>}}},{}},{{}}},{{{<!!a!!!!!!,a}!!9!,9oi!>,<o>},{}},{<{!!!!!>},<!!9!99!!!>!i!!,!>},<!>},<o!>},<,ia>,{<!>,<>,{<eu!!,!!!>a!!!!!>!!a!>,<}9!!!!{9!!!>>}}},{<!!!>!>,<>}},{{},{{{}},{{<,!<a!!}{<{>}}}}},{{{{{<>}},{{<!>e9!!!><!!a9<!!,!{o!ua!>},<i>},<!!!>u!!!!!>!!!>{!>o!eae}!!!!o!!o<!>,<9!>},<>},{}},{},{{},{{{<e!!u{o!>!!!!!>,<e!>!>!!!>9!u>}}}},{{{{<!!!>oe!!!!!>!!!>!o>},<!>!!9!!i!!<e!>!>!!!>a<!!9<!>,<i,u!!e>},{{{<!!!>,<a9!!!!{9uu!!!>}u!>>,{<9!>,<oeo!!,!>,<,a!!!!{<u!!!>u!uo!>>}}},{<!>i!>,<{!!!>,<{!!a!>>}},{{<9ia!e!!!!!!!>ua!>},<>},<!!!>!!,!>i>}},{{{{<!>!!{,>}},{<>,{<o9,>}},{{<>,<9!>,<uia!>!!9!>},<}9!99!>,<9}>}}},{<!!!>{{!9!>,<!!!!9i!!!>!>,<a>,{<i!>},<}!!u{!e!>>}}},{{<!!!>!!o{,oa>,<9u!>!{!!!!!>!>,<!!a!<ae!!!>!!!!9u<{!!!>>}},{{{<>,<!!>},{<,!>,<!!!!!>!>},<,9>}},{{<!!a}}!>},<o9,,i{ui9!!!>}o,u>}},{}}}},{{{<!!!!!i99!>},<<!9!!!>,9!!!>!!i!!,!!!!u>,{}}},{{<9!!!>}!>,<!!!>!!<>,{<eo9>,{{{{<}!!o!>,<{u!!!>>}},{<!!}9i!>},<9!!!>,<9,!>9!!!>!!!!!>9!ie!>!!{>}},<u!>},<}!!eo!!!!!e{!!!!,!>,<!!9{!>>}}}},{{<i>,{}}}}},{{{{<!!!>,<!>,<9!{>},{}}},{{{{<iio,!>,<a!>},<o!!,,a!!!!!>>},<!!!>i!<{!a!!ui!!!,<a!>>},{<!!9,>,<>}}}},{{{{}},{<!!!>a{!!!>}u!!!>},<!>},<99ie<!a{>,<a!!!>!>},<9}o!>!>},<!>9a,!!!><!>i9e9>}},{{{<!>9a!>,<o9!e!>,<}!u!!,!!9!>},<>}},{<u,!>!!!>9,a!!9}>,{}}}},{{{{{{},{{<9o>},{{<!o!>!!i!!!>!>,<!!!>!!u}i>},{<!!9!!!9e!>},<o!!!>ae!{!oi!}>}},{{{<!!!>},<!!e!uo{!>},<!!9}!aa<!>!>},<!!!>>},<!>,<e{9!>,<o>}}},{{{{{{<i!>},<!!!><!>,<{!!ou!!!e9a!>e!>},<<<!!e>}},{{<!!!>>}}},{}},{{{{{}},{<<u9!!!}}i>},{{},{{<<e9!!}!!!>}9<!!{!},>},{{{<!!!>},<,!!!>!a,o>},<ao9!!{e!}}}9!>,<!>,<,e99!}!9>},{{{}}}}}}},{{{},<e!>!>,<,u!>},<i!>!!!>,<<u!>,<!>,<9e<>}},{<},!i!>,<9u!>},<i!!!>,<!!!!!>!!!>!!},>}},{{<!>!>,<!!!i,u!!i!!!!<u!>,!>}o!!>,{}},{{{},<!>},<!!iu}o{!<!!,u9!>,<!!9}o,!>},<<9>},<!a9!!!!}!u}!>!>},<>}},{<o{,u!>},<!!i!o!!!>9{}!!!!,!o!>},<o},>,<a!{!>,<!!e!>!!{u>}},{{<9,!>,<a>},<}!>!!!>!!!>}e!!}!>},<o!!!>u99>}},{{{{{{},{{{}},{<!>o!>!!!>,o!!!>!!,e!!!!!>i!>,<,!>},<,!>,<i>}},{{}}},{},{<i,>,{<ea!!<>}}},{{<!!{i!>,<>},{{{<u!!!>9!>},<!!<!>},<ou}!u,!>},<}}!!!>},<}a>},<9}{,a{>}},{{<<!e!}!>,<!o!u!!!!!>,<!>,<!>9!>,<!>},<!!!>o!o!>{>},{<>}}},{{<<9!>,<!<!!9!!!>u}{a!!!>!>9!!!,o>}}},{<o}<!>,<!>},<<!>},<o!!!>!!!>{uu{i!!!!!>!>,<9>,{<,a9,9>}}},{{{{{<u!>,<}!<!!9u!i>},{<!!}}!!!>,<9!!9>}},{}},{{<!!!>o!!!>9u!>},<>,{<u!!,!u,i>}},{<!!!>{,e9!>,<uiie<<!!eo>}},{{<!>,<{<uo,9>},{<}}}>}}},{{{<ioi,,}{!>>},<9!!!!9!!9i!!!>,<!>,<a!>!>},<>},{{{<<!>},<!!<!!i,}!>,<!>,<9!!!>>,{}}}},{{<!>,<!!!!!>!>,!!!>,<>},{<o,u9ueoo!!<!>},<!>!>},<!!!!!>!>,<9>}}},{{{<99<{{!>,<!!>},{{{{},<>}},{{<!uu!o!>>}}}}}},{{{<9!>,<!>!i!9euu!>o!!!!,!{!!!!{!!!>!>},<!>,<}!>},<>},{<>,{<u!!!>!>},<!>},<}<u!>},<!>>}},{{<9!!!>,<}<<!e{i,!!!>!>,<!!!>!!!i!!!>,<!!{a!9{>},{<o9<!>,<e!!>}}},{},{{{<{{!!}9u!a{>},<!{<!>!!!!!>i99!!!>,<uu,}i!!!>>},{{},{{<!!!>9!!{>},<}!>!!{u9!!u9!!9!!u!!{,>},{{{<u>}},<!!!<!!!!<9o!!!>},<e>}},{{{<{{o!>,<i9e!>{!!u!>},<!o,>}}}}},{}},{{<!!!>!!!>9o9!!uie>}}}},{{{{},{{<99!!{!>,<!>},<!!}}>},<!>,<9!!,!!oi!!!>ieaa!!!>},<{9<!9!!u>}},{{<uea!>,<>},{}},{{},{{{}},{{{{},<!>},<!9,>}}}},{{<!!o,!>},<uii9<>}}}},{{{{<!!!!!>9<!!!>},<!>,<o99,!!<>}}},{{{},{{{<o{}!!!>!o!>,<9{,>}},<!>,<!>e}u!!>},{<!>},<9<}!>},<ieu!>},<<,!>e9!!e{9>}},{{<!!!!<!>,!!9oe!!<o<!!!>{!>,<9i!>},<,i}{>,<u!>,<9i!e!!!!!!!>},<o}9!>},<a>},{<!!!>a!>,<!!auuu!!a>,<!>,<!!!>a!>,<!!!>{e}<ee!>},<{>},{{}}},{{{<!>},<o!!ou!>},<!!999!!<<!a!!<}!!!>!!>},<i<,i}!e9!!}!!u!!<o>},{<<o!>!!,}<e!!!><>,{<{!>},<o,uuua>}},{{<,i!!!>}!!{!!a>},<,!!!>,<!!i}!e9},!>9!!!!!>!i!>,<!!!>!>,<o>}}},{{{<oua!}!!9{<!9!oa!!!>ia!>}!>,<>,<!>},<!>},<,!!u{i!!!>!>},<>},{{<9>}}},{<!>,,!!{!!!>!>!!!>!e{!!u!!{!!!>},<{}9!>!>ao>,<!99uu!{!!!>},<!>!u99!>},<}9!!oi>}}},{{<9!>,<,!>!!!>u>,{<>}},{<,!>9!!<!>!>{9au!!!>!ii!{!!!>}{oe>},{<!!u!!,uo!<!!,!!!}{}a!!ia>}},{{<>},{{},{}},{{{},{{{<>},{<o,u9!>!>,}i99}eo>}},{<i9!!!>o!!!>,<au!>9eo}e!!!!!>>}},{{<!!a!!9u!!!!!!!>!>{e}!>},<{!!<o>},{<}!>,<9u!!99{!!!>>}}}}}},{{<}!oo!>},<!i!!9}i9!!!>},<!>},<>},{{<>}}}},{{{{{}},{{<{}!!!!!>!!9<9!u}!!!>u}9e9,!!u!>!>},<!>,<>}}},{{<!>,<{io!>a!!9}}{i>},{<<9>}},{<!>,<!!{!!{!>},<>,{}}}}},{{{},{{<!!}u!>!!u{!o,>,{}},{{<{oa!>9!>,<!!,!>,<>,{{<a9!!<}!!!>!9!!u!}!>},<i!{oio!!!>>},{<!>},<i9>}}},{{<a9e!!!,}i!!9{u,!!!>9i!>},<>}}},{{<!>,<e!!>},{{<!>,<{,!!i!>,<,!{!>9,{,!!ii,!>},<>},{<!>},<!<<i!>},<!>!>},<9!eai!>,<!!!>,<9a<}<o>}}}},{{{{<9!e>},<<a!9e>},{},{{{<!>,<>}},{<,9!u!!e!>},<!>,<<ou9!>},<o>,{}},{}}},{{<,!!!9!>o!!!,>},{{<o9<!!a,,i!!!>!>},<!>,<!>o!>},<o{!!!>},<a}!>,<>},{{{{<9!!!>9u!!9!!a!!!!<{>},{<!>,<!>,<uue!!!>},<{9{o9!>,<!!!>!!{!>,<>}},{}},<u9!>!!u!>},<<<9!>o!>,<u9>},{{<!>>,<u,!>,<>},{<ai9!!!>!>,<i,a!!auu}!>},<,o!!!>},<u>,<<{o!!!!9a9,9!ie!!i!>!9!{!>>}}}},{{<{!!!>>,<,u9!oi,!>,<,ao!!!9999o!>>}}},{{<!!e9!!!>a9eu!!eee!>},<!!a!!!!,!!i!!!>!!e!!!>},<{>,<u!>,<<e!>,<,!!9!u!oaa!,!>},<a}!!!!}}>}}},{{{{{}},{<!!!>},<!>,<!!!>>}},{{{<<<a!>}9ao9!>,<i!o,}!!!>,<!!a,>},{}},{{<!!!!u<}!!!>>},<9!!!>},<>}},{{{}}},{{}}},{{{{<!{a!!i}!>},<{e!>},<i>}},{{<!!!>9<u!>,<!!!><>},<>}},{{<9!!!>}!!!>>},{{},{{<!,<i!!9uu!e}o>}}},{{},{<!!u!>},<!!e<u,!!!>!e!>!>!!!>9a,!>},<!>!!>}}},{{{{<,!!!>a!!a!>e!!9u!>,<!!!!{>}},{{<a!a!!99!!e9eu!o<!<!9!!oa!!!!!>{!>,<>}}},{{{<e9!!a!!!i!o!}u<!!!>aae>},{}},{<o<!>},<ue!>!o9!>,<aio>,<!!!>!!,ue!>,<!!!>},<o<!!<!!!!!>!>},<uu>},{{<u,{e9{>}}}},{{{{{<<9!a,<o>},{}}},{{<!!!<9,!!e!9!>!}!!9{}au9}!>},<!!!i>},{{{{},{<{!!!!!>!>},<!a!>>}},<!>,<>}},{<{e!!u!!e9!>!!!u!!e!>},<!!!>!>!!<!,>}},{{{{<!!u!>{9!>9!>!o!!e>},<!>i>},{{<!{!!!>,<{o>},{{{<9>}},{{<,{<a<aa!!!>ai!>>}}}},{<!>!o!u>,{}}},{{{{{<ui!>},<!!iu!>,<>}},<{!!e{a,<!!!><!!!!<o}ii!!!>},<!!!!!>oa>},{<!a<!uio!!!>ii!>},<{9!>}!!!>>,{<!!u!<!u!!e!!!>,<!!a,!!!>},<!!!!o!>},<,!>,<a{<>}},{{<!>!!euu!!ui!!9!>,<i!!9ae}9!!9!9>}}},{{<9!>oo!!!>},<!!!!o}!!i>},{}},{{<!!e9>}}}}},{{{<<!!!>ui!9!>,<e!!!!!{u<!!!>>}},{{{<e{o!!!!!><e,ou{}!!!9a<},>,{{<}!>,<{o!!!>e9<!i9!!!>!!!>,<!>9!>,<9!!!>!9>},{<>,{<!!{>}}}},{{},<!>,<!>},<!}>},{{{},<!>!>,<!!ai,uia!,{!!!>}!i!a!o9!!i>}}}},{{{}},{<!>e{}!>,<!!<{<9!!e,e{{!>},<!!!>},<!!!>,<e>,<9!!,!9!>,<,}ao>},{{{<!>a}!>o!!!>,9{!!u!>!>!!{9!>},<!!!>>,{<!>},<}!>,<uo!!9!!!>e,!!}!>i9!!}u!!oa!!9u>}}},{{},{<!!<!!!>},<!>,<!!!9{,!!9!>9a,9iie>,{}}},{{<!!!<!!99o!!!>i!>},<!!,!>9!!99e>}}}}},{{},{<io!>,<!!!>ai!!}9{>}}}},{{{{}},{{<!>,<!>,<i!!,!}!!>,<!>},<o>},{}},{{{<{io!!!><u}!o!>,!!!>},<!u<!!!><!!!>o>,<>},{<{9!!!>,<uu}!!!!!>>,{<i!!,!!!>},<!}!{!>},<!>o}!!<!>,<ao!>,<!>,<>}},{{},{<9{oa!,a,9u>}}},{<e!!!!e<u9>}},{{<<!>!>,<}9}a!!!>,ao}!9!>,<ue>,<9io!!!>,<o}>},{<<!>i>},{<<!!!!9!>},<!{a9u>,<!!!>}!>},<>}}},{{{{<!!e9u<!!!>},<!,a!!!{,!!!!>,<e!!!>!>},<,>},{<ae!o,9!!!>!!!>!!,!>},<e!!!>!!!>u,>},{{<!>},<o!>!>,e!>!>,<!>,<}!!ee!>a>},{}}},{{<<!>,<o!!!>!!u>},<9u!>},<!!!>},<o9i<a9!>},<o!>9>},{<!!!!!>,<ou}!>,<{,u!!!>,<!!!!a!i>}},{{{<!!{!>i!!!>!>,<{ai<!>},<eei!!!e>},{<o!>},<!!e9i!>},<!i<>}},{{},{{<!!uo!,99o!>},<}>},{<u9}!>},<}{!>},<!>},<}!>,<!!!a>}}},{},{{{<a!>},<9!>},<!!!>!!o9!>u!!9iau!!!!!!>}}}},{{<u!!9<!>},<a>}},{}},{{{{{<e!!!><!>i!!!!!>u!e!>},<!!!>,!u9,9{>,<!!!!!!a!!a!!<}!uo!>,<!!!!o!!!>,!!!!!>>},{{<99i!!<!eae!>},<9>}},{<!>},<a{9<!>,<o>}}},{<!!{{eo,!>,<9!{>,<9!>!>,<!>9a}!eio}9}!>},<<{!!>},{{<9uu<>},{<e>}}},{},{{{<!>},<uu!>!e!!!>au>,{{<,<},}!>},<,e!<u!!!>a<!9!>{!>},<!!!>>}}},{{{<,<>},{<!!!>},<<{o!!!!iu!io!!!!!>!>!}u!!!>!!!ei>}},{{<!!!>}!!!!<,9!>},<u>}},{}}}}}},{{{{{{<!>,<e!!a}!>!>,<e>},{<<}!>,<!!{e}ao!!!!!}>}},<9!>},<!!!>e<>},{<e!!!!!>!>},<!>!!a99!>},<i!!!!9i!><!>},<i!!!!!!}!>},<!>,<}>},{<9!!!!,o!!!!!!!!!u!>},<,!!>,{{<ii,!!i!>},<{>},{{<ou!!{i!!<>}}}}},{{{<ue,!!!>9!>},<9o!>},<o,u>},<!!!>,<}i!!!>},<o9}9!!!>a>},{},{{{}}}},{{{{<!9}o{!!!>!!!>u{!!uae>},{}},{},{{},<!!u<!!!>!>},<!!!!!>!>,<,!>},<e<u,!!>}},{}},{{{{<ie9<!!}<>},{{<{u{!>},<!9>},{<{9>}},{{},{}}}},{{{<9!>},<9!>},<u,}!>{!}!>},<i,}<}!!}>}}}}},{{{{{<!>e<!>},<<!>},<<!>},<>},{<i!>,<o!!i!!>}},{{},{<>}},{<>,<{!!!>!,<,!!u!!{!>,<o9!!!!9,9,!!!>o>}}},{{{{{<e!>},<a!{,!>,<e!>},<!>a!>,<!!!>o!!!>,!!!>>},{}},{{{<e!!!>,<ii9!!!>,<o{u>},{}}},{}},{{<e!>,<>}},{}},{{},{<,!u<}u!!<{!ea!>},<!o!o>,{}}}},{{<!!!,a>,<!!!!i<>},{<}e!o!!ei,!!!>9!!!>}}<!>,<o>,<!>,<!!!!!>!>},<i!9!<u!ee!>,<e!<9!>,<!!o!!!>},<>}},{{},{{{<>},{{},{}}}}}},{{{},{{<!o!!!}o<9,!>!>},<o!!!>},<>,<o!!}9!!<}a!>,<!>},<i{<99>}},{<!!o,9!>!!!>}{!>},<!>,<!>!!}{<!!>,<u<!!!9!>},<o9uo!!!>>}},{{{{{{<9!>},<a!oo!>,a!!i!!!>uu>}},{{<a!>}!>},<!>9!!{eoaaa!!9{!!!a,e>},{{},{{}},{{{<{!>!}9a9!>},<!>,<!>},<u{>}}}},{{},{{}}}},{<>,{{}}}},{{{{},{{{<<!>},<!>!!!>!>,<!!i!>!>!9{{e!!>},<oi!>},<{!!!>,<a!>},<!>}!!!!ua!!}!!e!>!!!e!>},<!o>},{<!>},<!>u!!>,{<!>},<o!i}o99{!u>}}},{{{<!!ai!>,<i>}},{}}},{{<o!>},<<!>i!!{}9i!>!!>}}},{{<!>,<e!>},<!>,<!!!>>},{<!>>}},{}},{{{{{<9!>,<!!!>},<!!,!>,<<i9a}!>,<!>,<o}u!!o!!!>},<!!!>>},{<{!{!!!>}!!<i!i!>,<99eu!!9a>}}}},<!>},<!>},<9<!>},<oou9!!ii9!e!!!>9>}},{{<!!e!>,<o!>!!!>{9!>},<a<!!!>!!u!!!>!!!>!!u{i>}},{{{<{<!>},<u!9!>},<i!!!>,<!!!!!>,<}e9<!>},<>}},{<!!!>},<9!!!>}9}9e>,{<!9{>}},{{<{>},{}}}}},{{<io!>},<i!{999i{,}!!!!!>!!!>!!!i<i>,{}}},{{{{<ei!!i!!>,{}},{<}!!!!i!!!>},<!!ei>},{{{{<{<,!ia!!!>9!>},<!>e}e!!!9>,{<!u9!>,<!>,<iu!!!>9!!9<<!>,<!>,<9!>},<99i!<>}},<!!{io!!!>{!!!>!!!!!!i!!!!,u!>>}},{{}},{{<!>!!!>u!!!>!>},<<i9!!o9!>a>,<<oe<}!9!>},<<}!>},<>},{{},<o!!!o99>}}}}},{},{{<,!<!>},<!>!!9!<!!!!!9aoa{!>>}}}},{{{{{{<o!>},<>},<u!!o9i!!u!!!>i!u9!>u>},{<!>,<!!!>e{!>},<a>,{<}!>,<u>,{<!>},<>}}}},{{{},<<e!!!>!!!>},<!>9>},{{{<!>!a}{{!!ua!!!>,<9iu>}},{{<e!o!>!!!a!>,<!!!>9!!!>!9u9{>}},{{<o!{u9>,<},u}a!>,<!!!9,o!>!!!>!>o{<>}}},{{<!>,<!u!>,!!!9!>!!!!!>!!!>!>!!!a!!!!!>!>},<,>},<!!,!>o!!!>9uu!>e!!!!!>!>},<i>}}},{{{},{<!!!!<{!}{9!!!>e!!!>{o!>9!!u!}!>>}},{{<<!!a!>aui>},<,a!!9e9,!!!}>},{{<!o{!!!!!>{!!!>o9>},{{<,9{!!,e9}!>,<e!>,<!!e>},{<9!>,<,!>},<u!>>},{}},{{}}}},{{{<!>9e{!!!>!!!>i9!>},<i!>,<>},{<u!>},<!>!>},<a9!!9!>},<>}},{{<<9u!>!><}!!!>{9!>},<99e9>}},{{},{{<{e<>},{<,uu!!!>9!>,<!,a>}}}}},{{<u,9!>,<!!!>eoe!!!>!>>}},{{{<9!>},<!!!>!!!>}!!e9}>},<o}}!!e!>i!i>},{{{<!>,<!>},<!!!!}>},{<!a,!{!>,<!>,<9!!i<>}},<e!>,<iu9!>,<}e!!!iao>},{}},{{{{{{},{{<!!<!>,<!!}9oo9!i<i,!!!>>}}},{{<{>},{{{<!>,<o9>},{<i!!!>!i!o!!e9e!>e,!>i!a9!>u!!!>>}}}}}}},{{<}!!!>o,!!!>!>a>,{<<a,,{>,<,!!!>}9!>},<!!!>!>!u!!!><!!9!!>}}},{{<o!!!>!<!!e!!a9!!uai!>a99!!!>e!>},<{>,{<ee!!,!>,<<>}},{<{a!>,<,i!>!!i!u},!!!>!!!!u}9>,{<>}},{{{{<!>},<!!99!>},<,,!>},<!!i!>,<!!9!>},<}!!9>},<!>},<ee!>},<,!>,<{!9!>,<u!!i!}>},{{<i!>},<i,!!!><o9u!>,!>},<!>},<o<!>ai!>>}},{}},{{{},<{o!>,<a!!<oe!!!>a>}},{<9!!!>!!!>>,{<{!!u,<}!>,<9o!}{ia9a!>,<eu>}}}}}}},{}},{{{{<!>},<!{!!!>o!!!!!!{!>},<,}9}9o!uo!!u9!!e>},{{{{<u!>,<!>!>{u!<99>,<i,,!,u!!!>i!!{!>,<!!a!!!>,<!>},<{9,>}},{<9,<!,!>}>}},{},{{{<<!9!!!>>},<9!>,<!>},<!!,9!>,<!!e!!!>!!<i,>},{{<!>},<!>,<ao}oe<>},<!!e!>,<o{!>,<}!!!>},<i!>},<u!!a!>,<!u}>},{}}}},{{<!>!>},<9!!9!!,!!o{}9e!!o!!!>!!!>9u>,<!>!9e}i!!!>!!!>!!a9,>}},{{<!!9!!!>{!>}9u!>,<<!!!!!>}e!!>},{<,u!!u!!!>!!<!>},<!!!>,<!!e{9,!!i!!!>!>},<!!o!99>}}},{{{<!>,<}99!>!>,<o<ui9>}},{{}}},{{<!i!!!iu!>},<i!a9,>},{<>,{}},{{<{!>},<e!!!>!!!>{ua!!!>!i!au!!!oi!!!>>}}}},{{{{},<}9i!!ae!!aiu!!e>}},{{<!!{!!{i!>!>,<!>,<e{}!!9>}},{{{<!!{!!u!>},<!,!i!!!>!{a<{<!>,a>},{<e!!!><,!!!><<!!<!<o>}},{{<!>{},<!!!u9!>,<!>9!>,<!!!>{{{i>},{{<!>9!!!!>}}}},{{{<}99o!9<!!!>>}},{},{<>,{{}}}}}},{{{{{{<!!!>!!o!!!>99>}},{{{<!!o!>,!>},<,i!!o!uooo!!,!!!!>}},<ai!>!>,<a!e{!>,<9!>,<a}9a>},{{{<!!}aoao}i!>9>},{<9!!}>}},{},{}}},{{}}},{{<!>},<!!i>},{}},{{<}!>!!!!!>}!!e}o}!!!>ue!!!>!>},<}!>},<,!>,<!>},<>,{{}}}},{{{{{<!>,<!!!!!!uu{!!!>e9ui!>},<<i!9u<>},{<!>i!!!!!!{!>o!!e,!!o!a!>},<}<!!!>},<!>},<!!!>,<>,<!>,<!!!!!>!}9ua!<!!!>e!!o,!>},<>}},{{<!!!!!>e}>},{<o>}}},{{{<,!>,<}}>}},{{{}},{{<,<ai!!!>},<e{>},<!!99!!u!!!>u!!!>a>},{{{<>}},{<,oi,!!,!!}!!!>!!,e!!!>,<i!>}{io}i!!u>}}},{{},{{},{{{{},{<!>,<!!9>}},{{<a!!e{,!>!>!>,<{e{a!>a>}}},{{{<o!!!!o<!>},<a!!!>!>9a!}!o!!!!}9,>},<{!!!>>}},{<{!>},<!!!!{!!o!>,<!>,ao<>,{<{a!>},<!>},<!>}o>}}}},{<e}!>,<!!!>,<o{i!e!!!>!!}u!!!>!!}o<!!!><{>,<i!>,<{i!!}!{!>,<!!!>!>},<>}}},{{{{<!!!u,,,a!e!!>},{<!>o>}},<!!!>9a!!o99!{}u!!i!>},<!!!>!!!>!!!>!>99!!>},{<!>,9!>u{!>,<<!!!>!>oi!>},<e}9>,<i}!!9,,<!!o>}}},{{<!!!!>,{}},{{<>}},{{<o!!!{!!!>,{!!i}!!o9!!a9{,>},<9u>}},{{{{<!!u!!!>>}},{{},{<!!{!>},<,a!o!!!>},<!>,<>}},{<!!!<iu!!{u!>{i!>},<!{e>,{<a!!!<!!o<e!>999!!!>9}!!a{>,{<!!ea!!!>ia9!!!>!!!!!!!>a9>,<o<{{!>,<ea{i!i9!!o9!!e!9!!u>}}}},{},{{{{<{{<9!!{!,9!>},<,a!!!>,<>},<99!>},<o,}!>},<iua>},{<u!!99!!!!!>!>}}{u!!!>{!>},<!!<!!!>>}},{{<9}ua!!9}}!>>},{}},{{},{<>}}}}}},{}},{{{{<>},<>},{{<!>>},{<!>,<<!!!>}!!!>ii<!>!!!>!!!>!!u!!!>!!9>}},{{<i!>},<>}}},{}}},{{{{},{{<!!eea{>}}},{{<!!{<!i<}9i9!>},<>}}}}}},{{{{<!>},<o!!!>o!!<!>}i!99!e>,{<!>,<o<>}},{},{{}}},{{{<ii!!!i}!>},<!!i>}},{{},{<<!oi,!!!>!!{<!>,!><9!!!>a>}}},{{{<!!!>ae!!!!!>},<oi!ue!>},<!!e}!>!!!>!>!}>}},{<i!>,<,!u!}>,<!!{e99o!>},<!!a!>ou!!!>!!i,!!!>>},{{<!!!>,<oo>}}},{{{<u}u<{!>,<!!!!!>!>},<{>}},{{<!!!>!e>,{}},{<i!>,<a!>,<!>,<i!>,<!!!e!>{<99!!u{!>},<,>,{<o9ae!!e!!e!!!>{i!>>}}},{<9!>!!9o!!9,{,u!!!!!>!>!>i<<>,{<!>{a!!!>!eu9}9!}!>,<}!>},<o!o>}}}},{{{<!>},<!>o<!e!>},<u!>},<{<!i!>,<}e>,{<u}i!!!!i{,o!>},<u!>>}},{<u!!!>,!!!>9},!>u}<}!>,<!!!!!>!!!>}9!!u!>,<>},{}},{{{}}},{{{<i!!!a!a!>},<u!>},<!>!>},<!>},<9!{!>!!!>!oo}!!!!!>u!>>},<!!!>o,>}}},{{{{<,u9!>},<{9!!{!!!>},<9!>},<!!!>!!,!>,<!!{!!9>}},{{{<,,,9!>!!9{i!!!!!!}>},<{!!!!!!!>e!>,<u!9<!>!>>},<,{>}},{{{}},{{<!>,<,!!,o!!,a!!!u>,{<!>!!!>!>},<9!!i>}},{<>}},{<u{!>},<>}},{{{{<9e!>!i9>},<!>9!>},<ue!>},<aa!>,<,!><!>},<o!>>},{{<!9!!<!>}>},{<a>}}}}}}}"

# eliminate the cancelled characters
cancellation_pat = re.compile(r"!.")
inp = re.sub(cancellation_pat, "", INPUT)


# eliminate the garbage
garbage_pat = re.compile(r"<[^>]*>")

inp = (
    re.sub(garbage_pat, "", inp).replace("{,", "{").replace(",}", "}").replace(" ", "")
)
inp = inp[1:-1]
# 1) the greedy way (used to solve the challenge) => O(n^2)

starttime= time.time()
count = 0
for i in range(len(inp)):
    if inp[i] == ',' and inp[:i].count("{") == inp[:i].count("}") :
        count += 1

print(f'{(method1_time := time.time() - starttime)} sec with the greedy method to find {count} outer-level commas')
# 2) more efficient way (should be O(n))
starttime= time.time()
open_brackets = 0
closing_brackets = 0
count = 0
for i in range(len(inp)):
    if inp[i] == '{':
        open_brackets += 1
    elif inp[i] == '}':
        closing_brackets += 1
    elif inp[i] ==',':
        if open_brackets == closing_brackets:
            count += 1 
        
print(f'''{(method2_time := time.time() - starttime)} sec with the more efficient method to find {count} outer-level commas,
that is {method1_time/method2_time} faster''')