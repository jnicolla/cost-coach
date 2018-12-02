import {mount} from '@vue/test-utils' 
import About from './About.vue'
describe ('About.vue',()=>
{
    test(' General Logic of Page', () => 
    {
        expect (true).toBe(true)
    })

    test('Checks to see if title for About page appeared and text is accurate', () => 
    {
       
        const wrapper = mount(About)
        const title = wrapper.find('#Title')
        expect (title.text()).toBe('About')
    })

}) 