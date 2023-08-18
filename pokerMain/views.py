from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Cards, utg_100bb, utg1_100bb, lj_100bb, hj_100bb, co_100bb, btn_100bb, scoring
import random
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    new_scoring = scoring(attempts=0, correct=0, score=0)
    new_scoring.save()
    model_id = new_scoring.id
    return render(request, 'pokerMain/index.html', {'model_id': model_id})

@login_required()
def play_game(request):
    random.randint(1, 52)
    # assigning random cards
    rand1 = random.randint(1, 52)
    rand2 = random.randint(1, 52)
    while rand1 == rand2:
        rand2 = random.randint(1, 52)
    card1 = Cards.objects.get(id=rand1)
    card2 = Cards.objects.get(id=rand2)

    # checking suits of cards, so we can check if hand is suited or not
    if card1.suit == card2.suit:
        suited = 'yes'
    else:
        suited = 'no'

    action = ''
    hands = ''
    # assigning random position each time game is played
    rand_position = random.randint(3, 8)
    if rand_position == 1:
        position_name = 'SB'
    if rand_position == 2:
        position_name = 'BB'
    if rand_position == 3:
        hands = utg_100bb.objects.all()
        position_name = 'UTG'
        table = '/images/images/poker table UTG.jpg'
    if rand_position == 4:
        hands = utg1_100bb.objects.all()
        position_name = 'UTG1'
        table = '/images/images/poker table UTG1.jpg'
    if rand_position == 5:
        hands = lj_100bb.objects.all()
        position_name = 'LJ'
        table = '/images/images/poker table LJ.jpg'
    if rand_position == 6:
        hands = hj_100bb.objects.all()
        position_name = 'HJ'
        table = '/images/images/poker table HJ.jpg'
    if rand_position == 7:
        hands = co_100bb.objects.all()
        position_name = 'CO'
        table = '/images/images/poker table CO.jpg'
    if rand_position == 8:
        hands = btn_100bb.objects.all()
        position_name = 'BTN'
        table = '/images/images/poker table BTN.jpg'

    for x in hands:
        # print(x.hand_name)
        # print(x.action)

        if suited == 'yes':
            if x.suited == 'yes':
                if card1.value == x.card1:
                    if card2.value == x.card2:
                        print('MATCH FOUND')
                        print(x.hand_name)
                        action = x.action
                        break

        if suited == 'yes':
            if x.suited == 'yes':
                if card1.value == x.card2:
                    if card2.value == x.card1:
                        print('MATCH FOUND')
                        print(x.hand_name)
                        action = x.action
                        break

        if suited == 'no':
            if x.suited == 'no':
                if card1.value == x.card2:
                    if card2.value == x.card1:
                        print('MATCH FOUND')
                        print(x.hand_name)
                        action = x.action
                        break

        if suited == 'no':
            if x.suited == 'no':
                if card1.value == x.card1:
                    if card2.value == x.card2:
                        print('MATCH FOUND')
                        print(x.hand_name)
                        action = x.action
                        break
        #print(x.suited)
        #print(card1)
        #print(card2)
        #print(x.hand_name)


    request.session['card1'] = card1.id
    request.session['card2'] = card2.id
    request.session['action'] = action
    request.session['table'] = table



    recent_score = scoring.objects.latest('id')

    attempts = recent_score.attempts
    correct = recent_score.correct
    score = recent_score.score
    score = score * 100
    score = round(score, 1)
    print(score)

    print("Card1 ID: " + str(card1.id))
    print("Card2 ID: " + str(card2.id))
    print("Action: " + str(action))
    print("Attempts:  " + str(attempts))
    print("Correct:  " + str(correct))
    print("Score:  " + str(score))

    return render(request, 'pokerMain/play.html', {'card1': card1, 'card2': card2, 'position_name': position_name,
                                                   'action': action, 'table': table, 'attempts': attempts,
                                                   'correct': correct, 'score': score})

@login_required()
def clicked_raise(request):
    action = request.session['action']
    card1_id = request.session['card1']
    card2_id = request.session['card2']
    table = request.session['table']

    print("Result Card1 ID: " + str(card1_id))
    print("Result Card2 ID: " + str(card2_id))
    print("final_result: " + action)

    newcard1 = Cards.objects.get(id=card1_id)
    newcard2 = Cards.objects.get(id=card2_id)

    recent_score = scoring.objects.latest('id')
    current_attempts= recent_score.attempts
    current_correct = recent_score.correct
    current_score = recent_score.score

    if action == 'raise':
        result = 'correct'
        current_correct += 1
    else:
        result = 'incorrect'

    if request.GET.get('Next Hand') == 'Next Hand':
        print('user clicked summary')

        current_attempts += 1
        current_score = current_correct / current_attempts

        recent_score.correct = current_correct
        recent_score.attempts = current_attempts
        recent_score.score = current_score
        recent_score.save()

        print("Attempts:  " + str(current_attempts))
        print("Correct:  " + str(current_correct))
        print("Score:  " + str(current_score))


        return redirect('pokerMain:play_game')

    return render(request, 'pokerMain/result.html', {'newcard1': newcard1, 'newcard2': newcard2, 'result': result,
                                                     'table': table})
@login_required()
def clicked_fold(request):
    action = request.session['action']
    card1_id = request.session['card1']
    card2_id = request.session['card2']
    table = request.session['table']

    print("Result Card1 ID: " + str(card1_id))
    print("Result Card2 ID: " + str(card2_id))
    print("final_result: " + action)

    newcard1 = Cards.objects.get(id=card1_id)
    newcard2 = Cards.objects.get(id=card2_id)

    recent_score = scoring.objects.latest('id')
    current_attempts = recent_score.attempts
    current_correct = recent_score.correct
    current_score = recent_score.score

    if action == 'fold':
        result = 'correct'
        current_correct += 1
    else:
        result = 'incorrect'

    if request.GET.get('Next Hand') == 'Next Hand':
        print('user clicked summary')
        current_attempts += 1
        current_score = current_correct / current_attempts

        recent_score.correct = current_correct
        recent_score.attempts = current_attempts
        recent_score.score = current_score
        recent_score.save()

        print("Attempts:  " + str(current_attempts))
        print("Correct:  " + str(current_correct))
        print("Score:  " + str(current_score))
        return redirect('pokerMain:play_game')

    return render(request, 'pokerMain/result.html', {'newcard1': newcard1, 'newcard2': newcard2, 'result': result,
                                                     'table':table})
@login_required()
def report_bug(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('pokerMain:play_game')

    return render(request, 'pokerMain/report.html', {'form': form})

@login_required()
def add_hands(request):
    # AA - A2s
    hand = btn_100bb(hand_name='AA', suited='no', card1='A', card2='A', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='AKs', suited='yes', card1='A', card2='K', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='AQs', suited='yes', card1='A', card2='Q', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='AJs', suited='yes', card1='A', card2='J', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A10s', suited='yes', card1='A', card2='10', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A9s', suited='yes', card1='A', card2='9', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A8s', suited='yes', card1='A', card2='8', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A7s', suited='yes', card1='A', card2='7', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A6s', suited='yes', card1='A', card2='6', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A5s', suited='yes', card1='A', card2='5', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A4s', suited='yes', card1='A', card2='4', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A3s', suited='yes', card1='A', card2='3', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A2s', suited='yes', card1='A', card2='2', action='raise')
    hand.save()

    # AKo - A2o
    hand = btn_100bb(hand_name='AKo', suited='no', card1='A', card2='K', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='AKos', suited='no', card1='A', card2='Q', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='AJo', suited='no', card1='A', card2='J', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A10o', suited='no', card1='A', card2='10', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A9o', suited='no', card1='A', card2='9', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A8o', suited='no', card1='A', card2='8', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A7o', suited='no', card1='A', card2='7', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A6o', suited='no', card1='A', card2='6', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='A5o', suited='no', card1='A', card2='5', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A4o', suited='no', card1='A', card2='4', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A3o', suited='no', card1='A', card2='3', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='A2o', suited='no', card1='A', card2='2', action='raise')
    hand.save()

    # KK - KQs
    hand = btn_100bb(hand_name='KK', suited='no', card1='K', card2='K', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='KQs', suited='yes', card1='K', card2='Q', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='KJs', suited='yes', card1='K', card2='J', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K10s', suited='yes', card1='K', card2='10', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K9s', suited='yes', card1='K', card2='9', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K8s', suited='yes', card1='K', card2='8', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K7s', suited='yes', card1='K', card2='7', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K6s', suited='yes', card1='K', card2='6', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K5s', suited='yes', card1='K', card2='5', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K4s', suited='yes', card1='K', card2='4', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K3s', suited='yes', card1='K', card2='3', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K2s', suited='yes', card1='K', card2='2', action='raise')
    hand.save()

    # KQo - K2o
    hand = btn_100bb(hand_name='KQo', suited='no', card1='K', card2='Q', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='KJo', suited='no', card1='K', card2='J', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K10o', suited='no', card1='K', card2='10', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K9o', suited='no', card1='K', card2='9', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K8o', suited='no', card1='K', card2='8', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K7o', suited='no', card1='K', card2='7', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K6o', suited='no', card1='K', card2='6', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K5o', suited='no', card1='K', card2='5', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='K4o', suited='no', card1='K', card2='4', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='K3o', suited='no', card1='K', card2='3', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='K2o', suited='no', card1='K', card2='2', action='fold')
    hand.save()

    # QQ-Q2s
    hand = btn_100bb(hand_name='QQ', suited='no', card1='Q', card2='Q', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='QJs', suited='yes', card1='Q', card2='J', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='Q10s', suited='yes', card1='Q', card2='10', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='Q9s', suited='yes', card1='Q', card2='9', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='Q8s', suited='yes', card1='Q', card2='8', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='Q7s', suited='yes', card1='Q', card2='7', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='Q6s', suited='yes', card1='Q', card2='6', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='Q5s', suited='yes', card1='Q', card2='5', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='Q4s', suited='yes', card1='Q', card2='4', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='Q3s', suited='yes', card1='Q', card2='3', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='Q2s', suited='yes', card1='Q', card2='2', action='raise')
    hand.save()

    # QJo - Q2o
    hand = btn_100bb(hand_name='QJo', suited='no', card1='Q', card2='J', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='Q10o', suited='no', card1='Q', card2='10', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='Q9o', suited='no', card1='Q', card2='9', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='Q8o', suited='no', card1='Q', card2='8', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='Q7o', suited='no', card1='Q', card2='7', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='Q6o', suited='no', card1='Q', card2='6', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='Q5o', suited='no', card1='Q', card2='5', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='Q4o', suited='no', card1='Q', card2='4', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='Q3o', suited='no', card1='Q', card2='3', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='Q2o', suited='no', card1='Q', card2='2', action='fold')
    hand.save()

    # JJ-J2s
    hand = btn_100bb(hand_name='JJ', suited='no', card1='J', card2='J', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='J10s', suited='yes', card1='J', card2='10', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='J9s', suited='yes', card1='J', card2='9', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='J8s', suited='yes', card1='J', card2='8', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='J7s', suited='yes', card1='J', card2='7', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='J6s', suited='yes', card1='J', card2='6', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='J5s', suited='yes', card1='J', card2='5', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='J4s', suited='yes', card1='J', card2='4', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='J3s', suited='yes', card1='J', card2='3', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='J2s', suited='yes', card1='J', card2='2', action='raise')
    hand.save()

    # J10o - J2o
    hand = btn_100bb(hand_name='J10o', suited='no', card1='J', card2='10', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='J9o', suited='no', card1='J', card2='9', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='J8o', suited='no', card1='J', card2='8', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='J7o', suited='no', card1='J', card2='7', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='J6o', suited='no', card1='J', card2='6', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='J5o', suited='no', card1='J', card2='5', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='J4o', suited='no', card1='J', card2='4', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='J3o', suited='no', card1='J', card2='3', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='J2o', suited='no', card1='J', card2='2', action='fold')
    hand.save()

    # TT - T2s
    hand = btn_100bb(hand_name='TT', suited='no', card1='10', card2='10', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='T9s', suited='yes', card1='10', card2='9', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='T8s', suited='yes', card1='10', card2='8', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='T7s', suited='yes', card1='10', card2='7', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='T6s', suited='yes', card1='10', card2='6', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='T5s', suited='yes', card1='10', card2='5', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='T4s', suited='yes', card1='10', card2='4', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='T3s', suited='yes', card1='10', card2='3', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='T2s', suited='yes', card1='10', card2='2', action='fold')
    hand.save()

    # T9o - T2o
    hand = btn_100bb(hand_name='T9o', suited='no', card1='10', card2='9', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='T8o', suited='no', card1='10', card2='8', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='T7o', suited='no', card1='10', card2='7', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='T6o', suited='no', card1='10', card2='6', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='T5o', suited='no', card1='10', card2='5', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='T4o', suited='no', card1='10', card2='4', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='T3o', suited='no', card1='10', card2='3', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='T2o', suited='no', card1='10', card2='2', action='fold')
    hand.save()

    # 99 - 92s
    hand = btn_100bb(hand_name='99', suited='no', card1='9', card2='9', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='98s', suited='yes', card1='9', card2='8', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='97s', suited='yes', card1='9', card2='7', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='96s', suited='yes', card1='9', card2='6', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='95s', suited='yes', card1='9', card2='5', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='94s', suited='yes', card1='9', card2='4', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='93s', suited='yes', card1='9', card2='3', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='92s', suited='yes', card1='9', card2='2', action='fold')
    hand.save()

    # 98o - 92o
    hand = btn_100bb(hand_name='98o', suited='no', card1='9', card2='8', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='97o', suited='no', card1='9', card2='7', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='96o', suited='no', card1='9', card2='6', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='95o', suited='no', card1='9', card2='5', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='94o', suited='no', card1='9', card2='4', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='93o', suited='no', card1='9', card2='3', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='92o', suited='no', card1='9', card2='2', action='fold')
    hand.save()

    # 88 - 82s
    hand = btn_100bb(hand_name='88', suited='no', card1='8', card2='8', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='87s', suited='yes', card1='8', card2='7', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='86s', suited='yes', card1='8', card2='6', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='85s', suited='yes', card1='8', card2='5', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='84s', suited='yes', card1='8', card2='4', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='83s', suited='yes', card1='8', card2='3', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='82s', suited='yes', card1='8', card2='2', action='fold')
    hand.save()

    # 87o - 82o
    hand = btn_100bb(hand_name='87o', suited='no', card1='8', card2='7', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='86o', suited='no', card1='8', card2='6', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='85o', suited='no', card1='8', card2='5', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='84o', suited='no', card1='8', card2='4', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='83o', suited='no', card1='8', card2='3', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='82o', suited='no', card1='8', card2='2', action='fold')
    hand.save()

    # 77 - 72s
    hand = btn_100bb(hand_name='77', suited='no', card1='7', card2='7', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='76s', suited='yes', card1='7', card2='6', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='75s', suited='yes', card1='7', card2='5', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='74s', suited='yes', card1='7', card2='4', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='73s', suited='yes', card1='7', card2='3', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='72s', suited='yes', card1='7', card2='2', action='fold')
    hand.save()

    # 76o - 72o
    hand = btn_100bb(hand_name='76o', suited='no', card1='7', card2='6', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='75o', suited='no', card1='7', card2='5', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='74o', suited='no', card1='7', card2='4', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='73o', suited='no', card1='7', card2='3', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='72o', suited='no', card1='7', card2='2', action='fold')
    hand.save()

    # 66 - 65s
    hand = btn_100bb(hand_name='66', suited='no', card1='6', card2='6', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='65s', suited='yes', card1='6', card2='5', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='64s', suited='yes', card1='6', card2='4', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='63s', suited='yes', card1='6', card2='3', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='62s', suited='yes', card1='6', card2='2', action='fold')
    hand.save()

    # 65o - 62o
    hand = btn_100bb(hand_name='65o', suited='no', card1='6', card2='5', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='64o', suited='no', card1='6', card2='4', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='63o', suited='no', card1='6', card2='3', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='62o', suited='no', card1='6', card2='2', action='fold')
    hand.save()

    # 55 - 52s
    hand = btn_100bb(hand_name='55', suited='no', card1='5', card2='5', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='54s', suited='yes', card1='5', card2='4', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='53s', suited='yes', card1='5', card2='3', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='52s', suited='yes', card1='5', card2='2', action='fold')
    hand.save()

    # 54o - 52o
    hand = btn_100bb(hand_name='54o', suited='no', card1='5', card2='4', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='53o', suited='no', card1='5', card2='3', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='52o', suited='no', card1='5', card2='2', action='fold')
    hand.save()

    # 44 - 42s
    hand = btn_100bb(hand_name='44', suited='no', card1='4', card2='4', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='43s', suited='yes', card1='4', card2='3', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='42s', suited='yes', card1='4', card2='2', action='fold')
    hand.save()

    # 43o - 42o
    hand = btn_100bb(hand_name='43o', suited='no', card1='4', card2='3', action='fold')
    hand.save()

    hand = btn_100bb(hand_name='42o', suited='no', card1='4', card2='2', action='fold')
    hand.save()

    # 33 - 32s
    hand = btn_100bb(hand_name='33s', suited='no', card1='3', card2='3', action='raise')
    hand.save()

    hand = btn_100bb(hand_name='32s', suited='yes', card1='3', card2='2', action='fold')
    hand.save()

    # 32o
    hand = btn_100bb(hand_name='32o', suited='no', card1='3', card2='2', action='fold')
    hand.save()

    # 22
    hand = btn_100bb(hand_name='22', suited='no', card1='2', card2='2', action='raise')
    hand.save()

    return render(request, 'pokerMain/addhands.html')