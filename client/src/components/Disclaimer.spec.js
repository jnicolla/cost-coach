import {mount} from '@vue/test-utils'
import Disclaimer from './Disclaimer.vue'
describe ('Disclaimer.vue',()=>
{
    it('Checks to see if Discalimer text is here', () => 
    {
       // expect (true).toBe(true)
        const wrapper = mount(Disclaimer)
        expect (wrapper.text()).toBe('Disclaimer Text: This is not a medically certified App. All the numebrs provided on this webpage are estimates')
        




    })
})

//Given (User is on the webpage)
// When (They try to go on the disclaimer page)
// Then (They should see the disclaimer Message)