import {mount} from '@vue/test-utils'
import Disclaimer from './Disclaimer.vue'
import More_Info from './Disclaimer.vue'
describe ('Disclaimer.vue',()=>
{
    it('Checks to see if Discalimer text is here', () => 
    {
        //Given (User is on the webpage)
        // When (They try to go on the disclaimer page)
        // Then (They should see the disclaimer Message)
       // expect (true).toBe(true)
        const wrapper = mount(Disclaimer)
        expect (wrapper.text()).toBe('Disclaimer Text: This is not a medically certified App. All the numebrs provided on this webpage are estimates  Read More')
    })

    it ('Checks to see if button is present and clickable', () => 
    {
         //Given (User is on the webpage)
        // When (They try to go on the disclaimer page)
        // Then (They should see the more information button)
        const wrapper = mount(More_Info) 
        wrapper.find('button')
    }) 
})

