from django import forms


question_list = [
    '1.我倾向从何处得到力量：',
    '2.当我参加一个社交聚会时，我倾向有更多的力气：',
    '3.下列哪一种听起来比较吸引人？',
    '4.在约会中，我通常：',
    '5.过去，我倾向遇见我大部分情人：',
    '6.我倾向拥有：',
    '7.过去，我爱的人和情人倾向对我说这些：',
    '8.我倾向透过以下方式收集信息',
    '9.我倾向相信：',
    '10.当我置身于一段关系中时，我倾向相信：',
    '11.当我对一个约会觉得放心时，我倾向谈论：',
    '12.我是这种人',
    '13.我是这种型的人：',
    '14.我通常',
    '15.我倾向如此做决定：',
    '16.我倾向比较能够察觉到：',
    '17.当和某人分手时。',
    '18.当与一个人交往时，我倾向评量：',
    '19.当我不同意我情人的想法时：',
    '20.认识我的人倾向形容我为：',
    '21.我把大部分和别人的相遇视为',
    '22.若我有时间和金钱，我的朋友邀请我到国外度假，并且在一天前才通知，我会：',
    '23.在第一次约会中，我：',
    '24.我偏好：',
    '25.我选择的生活循环着：',
    '26.哪一项较为常见：',
    '27我是这样喜欢(  )的人：',
    '28.我是这类型的人：',
                 ]
choices_list = [
    (('E', "别人。"),
     ('I', "我自己的想法。")),
    (('E', "在夜色很深时，一且我开始投入，也许就是最晚离开的那一个。"),
     ('I', "在夜晚开始的时候，我就疲倦了并且想回家。")),
    (('E', "与我的情人到有很多人且社交活动频繁的地方"),
     ('I', "待在家中与我的情人做一些特别的事情，例如说观赏一部有趣的录像带井享用我")),
    (('E', "整体来说蛮健谈的。"),
     ('I', "较安静并保留，直到我觉得舒服。")),
    (('E', '在宴会中、夜总会、工作上、体闲活动中、会议上、或当朋友介绍我给他们的朋友时。'),
     ('I', '透过私人的方式，例如个人厂广告、录像约会、或是由亲密的朋友和家人介绍。')),
    (('E', '很多认识的人和很亲密的朋友。'),
     ('I', '一些很亲密的朋友和一些认识的人')),
    (('E', '你难道不可以安静一点吗？'),
     ('I', '可以请你从你的世界中出来一下吗？')),
    (('N', '我对有可能发生之事的想象和期望。'),
     ('S', '我对目前状况实际认知。')),
    (('N', '我的直觉'),
     ('S', '我直接的观察和现成的经验。')),
    (('N', '水远有进步的空间。'),
     ('S', '若它没有被破坏，别修补它。')),
    (('N', '未来，关于改进或发明事物，和生活的种种可能性。例如说，我也许会谈论一个新的科学发明，或一个更好的方法来表达我的感受。'),
     ('S', '实际的，具体的，关于「此时此地」的事物。例如说，我也许会谈论品酒的好方法，或我即将参加的新奇旅程。')),
    (('N', '喜欢先看整个大局面。'),
     ('S', '喜欢先拿细节')),
    (('N', '与其活在现实中，我选择活在我的想象里。'),
     ('S', '与其活在我的想象里，我选择活在现实中。')),
    (('N', '偏向于去想象一大堆关于即将来临之约会的事情。'),
     ('S', '偏向于不急着想象即将来临的约会，只期待让它自然地发生')),
    (('F', '首先依我的心意，然后依我的逻辑。'),
     ('T', '首先依我的逐辑，然后依我的心意。')),
    (('F', '当人们需要情感上的支持时。'),
     ('T', '当人们不合逻辑时。')),
    (('F', '我通常让自己的情绪深陷其中，很难才能抽身而出。'),
     ('T', '虽然我觉得受伤，但一旦下定决心，我会直截了当地将过去恋人的影子甩开')),
    (('F', '情感上的兼容性：表达爱意和对另一半的需求很敏感。'),
     ('T', '智能上的兼容性：沟通重要的想法：客观地讨论和辩论事情')),
    (('F', '我尽可能地避免伤害对方的感受；若是会对对方造成伤害的话，我就不会说。'),
     ('T', '我通常毫无保留地说话，并且对我的情人直言直语，因为对的就是对的。')),
    (('F', '热情和故感'),
     ('T', '逻辑和明确。')),
    (('F', '友善及重要的'),
     ('T', '另有目的。')),
    (('J', '必须先检查我的时间表。'),
     ('P', '立即收拾行装。')),
    (('J', '若我所约的人来迟了，我会很不高兴。'),
     ('P', '一点都不在乎，因为我自己已常常退到。')),
    (('J', '事先知道约会的行程：要去哪里、有谁参加、我会在哪里多久、该如何打扮'),
     ('P', '让约会自然地发生，不做先前太多的计划。')),
    (('J', '日程表和组织。'),
     ('P', '自然发生和弹性。')),
    (('J', '我准时出席而其它人迟到。'),
     ('P', '其它人都准则出席而我退到')),
    (('J', '下定决心并且做出最后肯定的结论'),
     ('P', '开放我的选择并且持续收集信息。')),
    (('J', '喜欢在一个时间里专心于一件事情直到完成。'),
     ('P', '享受同时进行好几件事情')),
]


class MBTIForm(forms.Form):
    q0 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[0], label=question_list[0])
    q1 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[1], label=question_list[1])
    q2 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[2], label=question_list[2])
    q3 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[3], label=question_list[3])
    q4 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[4], label=question_list[4])
    q5 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[5], label=question_list[5])
    q6 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[6], label=question_list[6])
    q7 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[7], label=question_list[7])
    q8 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[8], label=question_list[8])
    q9 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[9], label=question_list[9])
    q10 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[10], label=question_list[10])
    q11 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[11], label=question_list[11])
    q12 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[12], label=question_list[12])
    q13 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[13], label=question_list[13])
    q14 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[14], label=question_list[14])
    q15 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[15], label=question_list[15])
    q16 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[16], label=question_list[16])
    q17 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[17], label=question_list[17])
    q18 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[18], label=question_list[18])
    q19 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[19], label=question_list[19])
    q20 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[20], label=question_list[20])
    q21 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[21], label=question_list[21])
    q22 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[22], label=question_list[22])
    q23 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[23], label=question_list[23])
    q24 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[24], label=question_list[24])
    q25 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[25], label=question_list[25])
    q26 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[26], label=question_list[26])
    q27 = forms.ChoiceField(widget=forms.RadioSelect, choices=choices_list[27], label=question_list[27])

    def __len__(self):
        return len(question_list)

