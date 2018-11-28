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

 
    test('Test to see if Button is viewable and clickable', () => 
    {
        const wrapper = mount(Home)
        const button = wrapper.find('#CalcButton')
        wrapper.trigger('click')    
        
    })

    test('Checks to see if text on button in V-card 1 is correct ', () => 
    {
       
        const wrapper = mount(Home)
        const but_1 = wrapper.find('#buttonText')
        expect (but_1.text()).toBe('Calculator')
        
    })

}) 