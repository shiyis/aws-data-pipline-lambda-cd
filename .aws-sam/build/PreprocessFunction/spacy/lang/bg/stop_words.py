"""
References:
    https://github.com/Alir3z4/stop-words - Original list, serves as a base.
    https://postvai.com/books/stop-dumi.pdf - Additions to the original list in order to improve it.
"""
STOP_WORDS = set(
    """
а автентичен аз ако ала

бе без беше би бивш бивша бившо бивши бил била били било благодаря близо бъдат
бъде бъда бяха

в вас ваш ваша вашата вашият вероятно вече взема ви вие винаги внимава време все 
всеки всички вместо всичко вследствие всъщност всяка втори във въпреки върху
вътре веднъж 

г ги главен главна главно глас го годно година години годишен

д да дали далеч далече два двама двамата две двете ден днес дни до добра добре 
добро добър достатъчно докато докога дори досега доста друг друга другаде други

е евтин едва един една еднаква еднакви еднакъв едно екип ето

живот жив

за здравей здрасти знае зная забавям зад зададени заедно заради засега заспал 
затова запазва започвам защо защото завинаги

и из или им има имат иска искам използвайки изглежда изглеждаше изглеждайки 
извън имайки

й йо 

каза казва казвайки казвам как каква какво както какъв като кога кауза каузи 
когато когото което които кой който колко която къде където към край кратък 
кръгъл

лесен лесно ли летя летиш летим лош

м май малко макар малцина междувременно минус ме между мек мен месец ми мис 
мисля много мнозина мога могат може мой можем мокър моля момента му

н на над назад най наш навсякъде навътре нагоре направи напред надолу наистина 
например наопаки наполовина напоследък нека независимо нас насам наскоро 
настрана необходимо него негов нещо нея ни ние никой нито нищо но нов някак нова 
нови новина някои някой някога някъде няколко няма

о обаче около описан опитах опитва опитвайки опитвам определен определено освен 
обикновено осигурява обратно означава особен особено от ох отвъд отгоре отдолу 
отново отива отивам отидох отсега отделно отколкото откъдето очевидно оттам 
относно още

п пак по повече повечето под поне просто пряко поради после последен последно 
посочен почти прави прав прави правя пред преди през при пък първата първи първо 
път пъти плюс

равен равна различен различни разумен разумно

с са сам само себе сериозно сигурен сигурно се сега си син скоро скорошен след 
следващ следващия следва следното следователно случва сме смях собствен 
сравнително смея според сред става срещу съвсем съдържа съдържащ съжалявам 
съответен съответно сте съм със също

т така техен техни такива такъв твърде там трета твой те тези ти то това 
тогава този той търси толкова точно три трябва тук тъй тя тях

у утре ужасно употреба успоредно уточнен уточняване

харесва харесали хиляди

ч часа ценя цяло цялостен че често чрез чудя

ще щеше щом щяха

юмрук

я як
""".split()
)