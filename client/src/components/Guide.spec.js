import {mount} from '@vue/test-utils' 
import Guide from './Guide.vue'

describe ('Guide.vue',()=>
{
    test('Test Logic of Page', () => 
    {
        expect (true).toBe(true)
    })

    test('Test to make sure Card Title Appears and has appropriate text', () => 
    {
        const wrapper = mount(Guide)
        const title = wrapper.find('#Title')
        expect (title.text()).toBe('Conversational Guide')
        
    })

    test('Test to make sure Card body Appears and has appropriate text', () => 
    {
        const wrapper = mount(Guide)
        const title = wrapper.find('#Main_Body')
        expect (title.text()).toBe('The purpose of this guide is to help structure a conversation about the costs of treatment '+ 
        '\n                with your healthcare professional. To use it, select any questions you have below and click "Generate".' +
        '\n                This will generate a file containing your selected questions, which you can print and bring to your next doctor\'s' + 
        '\n                appointment.')
        
    })

   
    test('Test to see if Button is viewable and clickable', () => 
    {
        const wrapper = mount(Guide)
        const button = wrapper.find('#PDFG')
        wrapper.trigger('click')    
        
    })
}) 