import nexmo

client = nexmo.Client(key='089e4c13', secret='aUgmlikQAhvlH0OF')

client.send_message({
    'from': 'Nexmo',
    'to': '255769191457',
    'text': 'Ndugu mteja tunapenda kukutaarifu kuwa utakosa maji kwa muda wa siku moja hivyo tunaomba ujaze vyombo vyako vizuri.... aisee kuwa maikini s',
})
