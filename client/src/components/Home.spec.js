import {mount} from '@vue/test-utils' 
import Home from './Home.vue'
describe ('Home.vue',()=>
{
    test('Logic of Page', () => 
    {
        expect (true).toBe(true)
    })

    test('Checks to see if intro V-card box 1 Appears', () => 
    {
       
        const wrapper = mount(Home)
        const box_1 = wrapper.find('#Card_1')
        expect (box_1.isVisible = true ) 
    })

    test('Checks to see if supplementary V-card box 2 Appears', () => 
    {
       
        const wrapper = mount(Home)
        const box_2 = wrapper.find('#Card_2')
        expect (box_2.isVisible = true ) 
    })

    test('Checks to see if supplementary V-card box 3 Appears', () => 
    {
       
        const wrapper = mount(Home)
        const box_3 = wrapper.find('#Card_3')
        expect (box_3.isVisible = true ) 
    })

    test('Checks to see if text on V-card 1 is correct ', () => 
    {
       
        const wrapper = mount(Home)
        const box_1 = wrapper.find('#Card_1')
        expect (box_1.text()).toBe('Welcome to CostCoach '+
        '\n                          CostCoach is the world\'s first application that can calculate your cancer treatment costs. ' + 
        '\n                          You only need three pieces of information to use it: your insurance plan, diagnosis, and medications.' + 
        '\n                          Press the button below and get started Calculator')
        
    })

 
    test('Test to see if Button  in vCard1 is viewable and clickable', () => 
    {
        const wrapper = mount(Home)
        const button = wrapper.find('#CalcButton')
        wrapper.trigger('click')    
        
    })

    test('Checks to see if text on button in V-card1 is correct ', () => 
    {
       
        const wrapper = mount(Home)
        const but_1 = wrapper.find('#buttonText')
        expect (but_1.text()).toBe('Calculator')
        
    })

    test('Test to see if Button in vCard2 is viewable and clickable', () => 
    {
        const wrapper = mount(Home)
        const button = wrapper.find('#GuideButton')
        wrapper.trigger('click')    
        
    })

    test('Checks to see if text on button in V-card2 is correct ', () => 
    {
       
        const wrapper = mount(Home)
        const but_2 = wrapper.find('#gButtonText')
        expect (but_2.text()).toBe('Guide')
        
    })
    test('Checks to see if text on V-card 1 is correct ', () => 
    {
       
        const wrapper = mount(Home)
        const box_1 = wrapper.find('#Card_1')
        expect (box_1.text()).toBe('Welcome to CostCoach '+
        '\n                          CostCoach is the world\'s first application that can calculate your cancer treatment costs. ' + 
        '\n                          You only need three pieces of information to use it: your insurance plan, diagnosis, and medications.' + 
        '\n                          Press the button below and get started Calculator')
        
    })

    test('Checks to see if text on V-card 2 is correct ', () => 
    {
       
        const wrapper = mount(Home)
        const box_2 = wrapper.find('#Card_2')
        expect (box_2.text()).toBe('Fighting the Stigma '+
        '\n                          Having a conversation with your health care provider about finances can be challenging. To make ' + 
        '\n                          this conversation easier, a list of common questions have been assembled in our Guide.' +
        '\n                          Find your questions here Guide')
        
    })

    test('Checks to see if text on V-card 3 is correct ', () => 
    {
       
        const wrapper = mount(Home)
        const box_3 = wrapper.find('#Card_3')
        expect (box_3.text()).toBe('Did you know? '+
        '\n                          The Agency for Healthcare Research and Quality (AHRQ) estimates that the direct medical costs '+
        '\n                          (total of all health care costs) for cancer in the US in 2015 were ' +
        '\n                          $80.2 billion.'+
        '\n                         52 percent of patients desire a cost discussion with their oncologist.'+
        '\n                         57 percent of patients reported lower treatment costs due to a discussion.'+
        '\n                         19 percent of patients actually have a cost discussion.'
        )
        
    })
}) 