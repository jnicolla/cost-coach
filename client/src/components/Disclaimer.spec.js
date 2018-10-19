import {mount} from '@vue/test-utils'
import Disclaimer from './Disclaimer.vue'
describe ('Disclaimer.vue',()=>
{
    it('is third', () => 
    {
       // expect (true).toBe(true)
        const wrapper = mount(Disclaimer)
        expect (wrapper.text()).toBe('Disclaimer Text: This is not a medically certified App')
        




    })
})