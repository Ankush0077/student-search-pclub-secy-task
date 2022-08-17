from django.shortcuts import render
from django.db.models import Q
from .models import Student
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.
def student_search(request):  
    if request.method=='POST':
        name=request.POST.get('name')
        hometown=request.POST.get('hometown')
        Ap=request.POST.get('A+')
        An=request.POST.get('A-')
        ABp=request.POST.get('AB+')
        ABn=request.POST.get('AB-')
        Bp=request.POST.get('B+')
        Bn=request.POST.get('B-')
        Op=request.POST.get('O+')
        On=request.POST.get('O-')
        blood_group_list1=[Ap,An,ABp,ABn,Bp,Bn,Op,On]
        blood_group_list2=['A+','A-','AB+','AB-','B+','B-','O+','O-']
        blood_group_list3=[]
        ae=request.POST.get('Aerospace Engineering')
        bsbe=request.POST.get('Biological Sciences and Bioengineering')
        ce=request.POST.get('Civil Engineering')
        che=request.POST.get('Chemical Engineering')
        chm=request.POST.get('Chemistry')
        cse=request.POST.get('Computer Science and Engineering')
        cgs=request.POST.get('Cognitive Sciences')
        doaa=request.POST.get('Dean Of Academic Affairs')
        dora=request.POST.get('Dean Of Resource Affairs')
        dord=request.POST.get('Dean Of Research and Development')
        eco=request.POST.get('Economic Sciences')
        ee=request.POST.get('Electrical Engineering')
        eem=request.POST.get('EEM')
        es=request.POST.get('Earth Sciences')
        hss=request.POST.get('Humanities and Social Sciences')
        ime=request.POST.get('Industrial and Management Engineering')
        lt=request.POST.get('Laser Technology')
        mdes=request.POST.get('MDes')
        me=request.POST.get('Mechanical Engineering')
        mse=request.POST.get('Material Science and Engineering')
        mas=request.POST.get('Mathematics & Statistics')
        mme=request.POST.get('Mat. and Met.Engg.')
        msp=request.POST.get('Materials Science Programme')
        masc=request.POST.get('Mathematics And Scientific Comp')
        neatp=request.POST.get('Nuc. Engg. and Tech Prog.')
        nullp=request.POST.get('Null')
        phy=request.POST.get('Physics')
        psae=request.POST.get('Photonics Science and Engg.')
        stats=request.POST.get('Statistics')
        sds=request.POST.get('Statistics And Data Science')
        see=request.POST.get('Sustainable Energy Engineering')
        branch_list1=[ae,bsbe,ce,che,chm,cse,cgs,doaa,dora,dord,eco,ee,eem,es,hss,ime,lt,mdes,me,mse,mas,mme,msp,masc,neatp,nullp,phy,psae,stats,sds,see]
        branch_list2=[
        'Aerospace Engineering',
        'Biological Sciences and Bioengineering',
        'Civil Engineering',
        'Chemical Engineering',
        'Chemistry',
        'Computer Science and Engineering',
        'Cognitive Sciences',
        'Dean Of Academic Affairs',
        'Dean Of Resource Affairs',
        'Dean Of Research and Development',
        'Economic Sciences',
        'Electrical Engineering',
        'EEM',
        'Earth Sciences',
        'Humanities and Social Sciences',
        'Industrial and Management Engineering',
        'Laser Technology',
        'MDes',
        'Mechanical Engineering',
        'Material Science and Engineering',
        'Mathematics and Statistics',
        'Mat. and Met.Engg.',
        'Materials Science Programme',
        'Mathematics And Scientific Comp',
        'Nuc. Engg. and Tech Prog.',
        'Null',
        'Physics',
        'Photonics Science and Engg.',
        'Statistics',
        'Statistics And Data Science',
        'Sustainable Energy Engineering',
        ]
        branch_list3=[]
        bs=request.POST.get('BS')
        bsmba=request.POST.get('BS-MBA')
        bsms=request.POST.get('BS-MS')
        bsmt=request.POST.get('BS-MT')
        btmdes=request.POST.get('BT-M.Des')
        btmba=request.POST.get('BT-MBA')
        btms=request.POST.get('BT-MS')
        btech=request.POST.get('B.Tech')
        diit=request.POST.get('DIIT')
        ep=request.POST.get('Exchange Programme')
        mba=request.POST.get('MBA')
        MDes=request.POST.get('M.Des')
        msr=request.POST.get('MS-Research')
        msc2=request.POST.get('MSc(2 yr)')
        msci=request.POST.get('MSc(Int)')
        mscphddual=request.POST.get('MSc-PhD(Dual)')
        mtdual=request.POST.get('MT(Dual)')
        mtech=request.POST.get('M.Tech')
        pgpexvlm=request.POST.get('PGPEX-VLM')
        phd=request.POST.get('PhD')
        prep=request.POST.get('Prep.')
        surge=request.POST.get('SURGE')
        emasters=request.POST.get('eMasters')
        programme_list1=[bs,
        bsmba,
        bsms,
        bsmt,
        btmdes,
        btmba,
        btms,
        btech,
        diit,
        ep,
        mba,
        MDes,
        msr,
        msc2,
        msci,
        mscphddual,
        mtdual,
        mtech,
        pgpexvlm,
        phd,
        prep,
        surge,
        emasters,]
        programme_list2=[
        'BS',
        'BS-MBA',
        'BS-MS',
        'BS-MT',
        'BT-M.Des',
        'BT-MBA',
        'BT-MS',
        'B.Tech',
        'DIIT',
        'Exchange Programme'
        'MBA',
        'M.Des',
        'MS-Research',
        'MSc(2 yr)',
        'MSc(Int)',
        'MSc-PhD(Dual)',
        'MT(Dual)',
        'M.Tech',
        'PGPEX-VLM',
        'PhD',
        'Prep.',
        'SURGE',
        'eMasters',
        ]
        programme_list3=[]
        hall1=request.POST.get('HALL 1')
        hall2=request.POST.get('HALL 2')
        hall3=request.POST.get('HALL 3')
        hall4=request.POST.get('HALL 4')
        hall5=request.POST.get('HALL 5')
        hall6=request.POST.get('HALL 6')
        hall7=request.POST.get('HALL 7')
        hall8=request.POST.get('HALL 8')
        hall9=request.POST.get('HALL 9')
        hall10=request.POST.get('HALL 10')
        hall11=request.POST.get('HALL 11')
        hall12=request.POST.get('HALL 12')
        hall13=request.POST.get('HALL 13')
        gh=request.POST.get('GH')
        day=request.POST.get('DAY')
        cpwd=request.POST.get('CPWD')
        aces=request.POST.get('ACES')
        nra=request.POST.get('NRA')
        ra=request.POST.get('RA')
        sbra=request.POST.get('SBRA')
        type1=request.POST.get('TYPE 1')
        type1b=request.POST.get('TYPE 1B')
        unkn=request.POST.get('UNKN')
        hall_list1=[hall1,hall2,hall3,hall4,hall5,hall6,hall7,hall8,hall9,hall10,hall11,hall12,hall13,gh,day,cpwd,aces,nra,ra,sbra,type1,type1b,unkn]
        hall_list2=[
        'HALL 1',
        'HALL 2',
        'HALL 3',
        'HALL 4',
        'HALL 5',
        'HALL 6',
        'HALL 7',
        'HALL 8',
        'HALL 9',
        'HALL 10',
        'HALL 11',
        'HALL 12',
        'HALL 13',
        'GH',
        'DAY',
        'CPWD',
        'ACES',
        'NRA',
        'RA',
        'SBRA',
        'TYPE 1',
        'TYPE 1B',
        'UNKN',
        ]
        hall_list3=[]
        male=request.POST.get('Male')
        female=request.POST.get('Female')
        gender_list1=[male,female]
        gender_list2=['Male','Female']
        gender_list3=[]
        y22=request.POST.get('Y22')
        y21=request.POST.get('Y21')
        y20=request.POST.get('Y20')
        y19=request.POST.get('Y19')
        y18=request.POST.get('Y18')
        y17=request.POST.get('Y17')
        y16=request.POST.get('Y16')
        y15=request.POST.get('Y15')
        y14=request.POST.get('Y14')
        y13=request.POST.get('Y13')
        y12=request.POST.get('Y12')
        y11=request.POST.get('Y11')
        y10=request.POST.get('Y10')
        y9=request.POST.get('Y9')
        y8=request.POST.get('Y8')
        other=request.POST.get('Other')
        year_list1=[y22,y21,y20,y19,y18,y17,y16,y15,y14,y13,y12,y11,y10,y9,y8,other]
        year_list2=[
        'Y22',
        'Y21',
        'Y20',
        'Y19',
        'Y18',
        'Y17',
        'Y16',
        'Y15',
        'Y14',
        'Y13',
        'Y12',
        'Y11',
        'Y10',
        'Y9',
        'Y8',
        'Other',
        ]
        year_list3=[]
        try:
            blood_group_length = len(blood_group_list1)
            for i in range(0,blood_group_length):
                if blood_group_list1[i]!=None:
                    blood_group_list3.append(blood_group_list2[i])
            blood_group_Q=Q(blood_group__in=blood_group_list3)
            branch_length = len(branch_list1)
            for i in range(0,branch_length):
                if branch_list1[i]!=None:
                    branch_list3.append(branch_list2[i])
            branch_Q=Q(branch__in=branch_list3)
            programme_length = len(programme_list1)
            for i in range(0,programme_length):
                if programme_list1[i]!=None:
                    programme_list3.append(programme_list2[i])
            programme_Q=Q(programme__in=programme_list3)
            hall_length = len(hall_list1)
            for i in range(0,hall_length):
                if hall_list1[i]!=None:
                    hall_list3.append(hall_list2[i])
            hall_Q=Q(hall__in=hall_list3)
            gender_length = len(gender_list1)
            for i in range(0,gender_length):
                if gender_list1[i]!=None:
                    gender_list3.append(gender_list2[i])
            gender_Q=Q(gender__in=gender_list3)
            year_length = len(year_list1)
            for i in range(0,year_length):
                if year_list1[i]!=None:
                    year_list3.append(year_list2[i])
            year_Q=Q(year__in=year_list3)
            if len(year_list3)!=0:
                if len(gender_list3)!=0:
                    if len(hall_list3)!=0:
                        if len(programme_list3)!=0:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q&programme_Q&hall_Q&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q&hall_Q&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q&hall_Q&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q&programme_Q&hall_Q&gender_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q&programme_Q&hall_Q&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q&programme_Q&hall_Q&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q&programme_Q&hall_Q&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q&programme_Q&hall_Q&gender_Q&year_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&programme_Q&hall_Q&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&programme_Q&hall_Q&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&programme_Q&hall_Q&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&programme_Q&hall_Q&gender_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&programme_Q&hall_Q&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&programme_Q&hall_Q&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&programme_Q&hall_Q&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(programme_Q&hall_Q&gender_Q&year_Q).values()
                        else:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q&hall_Q&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&hall_Q&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&hall_Q&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q&hall_Q&gender_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q&hall_Q&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q&hall_Q&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q&hall_Q&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q&hall_Q&gender_Q&year_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&hall_Q&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&hall_Q&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&hall_Q&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&hall_Q&gender_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&hall_Q&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&hall_Q&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&hall_Q&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(hall_Q&gender_Q&year_Q)
                    else:
                        if len(programme_list3)!=0:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q&programme_Q&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q&programme_Q&gender_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q&programme_Q&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q&programme_Q&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q&programme_Q&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q&programme_Q&gender_Q&year_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&programme_Q&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&programme_Q&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&programme_Q&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&programme_Q&gender_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&programme_Q&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&programme_Q&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&programme_Q&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(programme_Q&gender_Q&year_Q).values()
                        else:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q&gender_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q&gender_Q&year_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&gender_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&gender_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&gender_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&gender_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(gender_Q&year_Q) 
                else:
                    if len(hall_list3)!=0:
                        if len(programme_list3)!=0:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q&programme_Q&hall_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q&hall_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q&hall_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q&programme_Q&hall_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q&programme_Q&hall_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q&programme_Q&hall_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q&programme_Q&hall_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q&programme_Q&hall_Q&year_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&programme_Q&hall_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&programme_Q&hall_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&programme_Q&hall_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&programme_Q&hall_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&programme_Q&hall_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&programme_Q&hall_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&programme_Q&hall_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(programme_Q&hall_Q&year_Q).values()
                        else:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q&hall_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&hall_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&hall_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q&hall_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q&hall_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q&hall_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q&hall_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q&hall_Q&year_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&hall_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&hall_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&hall_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&hall_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&hall_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&hall_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&hall_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(hall_Q&year_Q)
                    else:
                        if len(programme_list3)!=0:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q&programme_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q&programme_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q&programme_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q&programme_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q&programme_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q&programme_Q&year_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&programme_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&programme_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&programme_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&programme_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&programme_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&programme_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&programme_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(programme_Q&year_Q).values()
                        else:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q&year_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&year_Q&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&year_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&year_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&year_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&year_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&year_Q).values()
                                    else:
                                        student=Student.objects.filter(year_Q)
            else:
                if len(gender_list3)!=0:
                    if len(hall_list3)!=0:
                        if len(programme_list3)!=0:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q&programme_Q&hall_Q&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q&hall_Q&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q&hall_Q&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q&programme_Q&hall_Q&gender_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q&programme_Q&hall_Q&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q&programme_Q&hall_Q&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q&programme_Q&hall_Q&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q&programme_Q&hall_Q&gender_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&programme_Q&hall_Q&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&programme_Q&hall_Q&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&programme_Q&hall_Q&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&programme_Q&hall_Q&gender_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&programme_Q&hall_Q&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&programme_Q&hall_Q&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&programme_Q&hall_Q&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(programme_Q&hall_Q&gender_Q).values()
                        else:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q&hall_Q&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&hall_Q&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&hall_Q&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q&hall_Q&gender_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q&hall_Q&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q&hall_Q&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q&hall_Q&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q&hall_Q&gender_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&hall_Q&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&hall_Q&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&hall_Q&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&hall_Q&gender_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&hall_Q&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&hall_Q&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&hall_Q&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(hall_Q&gender_Q)
                    else:
                        if len(programme_list3)!=0:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q&programme_Q&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q&programme_Q&gender_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q&programme_Q&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q&programme_Q&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q&programme_Q&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q&programme_Q&gender_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&programme_Q&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&programme_Q&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&programme_Q&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&programme_Q&gender_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&programme_Q&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&programme_Q&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&programme_Q&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(programme_Q&gender_Q).values()
                        else:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q&gender_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q&gender_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&gender_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&gender_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&gender_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&gender_Q).values()
                                    else:
                                        student=Student.objects.filter(gender_Q) 
                else:
                    if len(hall_list3)!=0:
                        if len(programme_list3)!=0:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q&programme_Q&hall_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q&hall_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q&hall_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q&programme_Q&hall_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q&programme_Q&hall_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q&programme_Q&hall_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q&programme_Q&hall_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q&programme_Q&hall_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&programme_Q&hall_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&programme_Q&hall_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&programme_Q&hall_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&programme_Q&hall_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&programme_Q&hall_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&programme_Q&hall_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&programme_Q&hall_Q).values()
                                    else:
                                        student=Student.objects.filter(programme_Q&hall_Q).values()
                        else:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q&hall_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&hall_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&hall_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q&hall_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q&hall_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q&hall_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q&hall_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q&hall_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&hall_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&hall_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&hall_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&hall_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&hall_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&hall_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&hall_Q).values()
                                    else:
                                        student=Student.objects.filter(hall_Q)
                    else:
                        if len(programme_list3)!=0:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q&programme_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q&programme_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q&programme_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q&programme_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q&programme_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q&programme_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q&programme_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&programme_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&programme_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&programme_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&programme_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&programme_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&programme_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&programme_Q).values()
                                    else:
                                        student=Student.objects.filter(programme_Q).values()
                        else:
                            if len(branch_list3)!=0: 
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q&branch_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q&branch_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q&branch_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q&branch_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&branch_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&branch_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&branch_Q).values()
                                    else:
                                        student=Student.objects.filter(branch_Q).values()
                            else:
                                if len(blood_group_list3)!=0:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))&blood_group_Q).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)&blood_group_Q).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)&blood_group_Q).values()
                                    else:
                                        student=Student.objects.filter(blood_group_Q).values()
                                else:
                                    if hometown=='' and name!='':
                                        student=student=Student.objects.filter(((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name)))).values()
                                    elif name=='' and hometown!='':
                                        student=Student.objects.filter(Q(hometown__icontains=hometown)).values()
                                    elif name!='' and hometown!='':
                                        student=Student.objects.filter((Q(name__icontains=name)|Q(roll_no__icontains=name)|Q(userid__icontains=name))&Q(hometown__icontains=hometown)).values()
                                    else:
                                        student=Student.objects.filter(roll_no='Ankush') 
        except:
            print('except')
            student=Student.objects.filter(roll_no='Ankush')
    else:
        student=Student.objects.filter(roll_no='Ankush')
    count=student.count()
    if(count==0):
        empty=True
    else:
        empty=False
    context={
        'student': student,
        'empty': empty,
        'length': count,
    }
    return render(request, "index.html", context)

def family_tree(request, roll_no):
    student=Student.objects.filter(roll_no=roll_no)
    print(student)
    student=student.get(roll_no=roll_no)
    try:
        baapuRoll=student.student_guide.roll_no
        print(baapuRoll)
        baapu=Student.objects.get(roll_no=baapuRoll)
        print(baapu)
        bhai=Student.objects.filter(student_guide=baapu).exclude(roll_no=roll_no)
        baapu_present=True
        if student.gender=='Female':
            baapuText='Amma'
            bhaiText='Behen'
        else:
            baapuText='Baapu'  
            bhaiText='Bhai'
    except:
        baapu=None
        bhai=[]
        baapu_present=False
    bacha=Student.objects.filter(student_guide=student)
    context={
        'student': student,
        'baapu':baapu,
        'bhai': bhai,
        'bacha': bacha,
        'baapu_present': baapu_present,
        'baapu_text': baapuText,
        'bhai_text': bhaiText,
    }
    return render(request,"family_tree.html",context)