import {mount} from '@vue/test-utils' 
import Disclaimer from './Disclaimer.vue'
describe ('Disclaimer.vue',()=>
{
    test(' General Logic of Page', () => 
    {
        expect (true).toBe(true)
    })

    test('Checks to see if title for Disclaimer page appeared and text is accurate', () => 
    {
       
        const wrapper = mount(Disclaimer)
        const title = wrapper.find('#Title')
        expect (title.text()).toBe('Privacy Policy')
    })
    test('Checks to see if Discalimer main body text is present on V-card and text is accurate', () => 
    {
       // expect (true).toBe(true)
        const wrapper = mount(Disclaimer)
        const title = wrapper.find('#Main_Body')
        expect (title.text()).toBe('CostCoach collects information on your insurance plan, your diagnosis, and your medications. However, it does not '+ 
        '\n                    collect any identifying information and does not store the information you provide.')

    })

}) 


