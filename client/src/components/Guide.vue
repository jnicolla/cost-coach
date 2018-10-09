<template>
<div>
    <center> <h1 class="md-display-3">Conversation Guideline</h1></center><center> <font color="md-accent">Below are common questions that a patient can ask their doctor or FCC to better understand their treatment cost.</font></center>
 <center> <font color="white">.</font></center>
 <center> <font color="white">.</font></center>
 <center> <font color="white">.</font></center>



  <VueFaqAccordion 
    :items="myItems"
  />
</div>
</template>
 
<script>
import VueFaqAccordion from 'vue-faq-accordion'
 
export default {
  components: {
    VueFaqAccordion
  },
  data () {
    return {
      myItems: [
          {
            title: 'What is my prescription co-pay for this drug?',
            value: '$40',
            category: 'Treatment Questions'
          },
          {
            title: 'Can I switch to a less expensive brand-name drug within the same drug class?',
            value: 'Yes, if you contact your FCC they can help you determine if there are cheaper alterantives to the medication your taking',
            category: 'Treatment Questions'
          },
          {
            title: 'What is the best way to contanct my oncologist',
            value: 'The best way would be to schedulea  meeting to talk to them',
            category: 'Treatment Questions'
          },
          {
            title: 'How long do labratory tests last?',
            value: '2-3 hours',
            category: 'Treatment Questions'
          },
          {
            title: 'How many times do I take my medicine?',
            value: '7 times a day',
            category: 'Treatment Questions'
          },
          {
            title: 'Who can I speak to about my health insurance questions and concerns?',
            value: 'You can talk to your FCC or your insurance provider. The Duke Cancer FCC department can be reached at: 919-212-1221 ',
            category: 'Finance Questions'
          },
          {
            title: 'Who can help me work with my health insurance provider?',
            value: 'Financial Cousling something',
            category: 'Finance Questions'
          }, 
           {
            title: 'How much is my co-pay for each doctor visit?',
            value: 'That is a tricky question as your co-pay depends on your insurance type',
            category: 'Finance Questions'
          },
           {
            title: 'When is payment due?',
            value: 'Your payment dates are arranged by your insurance and are ususally once a month',
            category: 'Finance Questions'
          },
           {
            title: 'Who can help me estimate the total cost of the recommended treatment plan?',
            value: 'Your FCC, insurance counsleor, and this app',
            category: 'Finance Questions'
          },
           {
            title: 'What expenses does my health insurance cover if I need to be admitted to the hospital?',
            value: 'Your insurance will cover the following values depending on the type of cancer treatment + other stuff',
            category: 'Finance Questions'
          }
          
        ]
    }
  }
}
</script>

props: {
 
  /**
   * Array of items
   * Object style {questionProperty: string, answerProperty: string, tabName: string}
   * You can change object keys names using other props (questionProperty, answerProperty, tabName)
   */
  items: {
    type: Array,
    required: true
  },
 
  /**
   * Key name of object in items array for specifying title of question
   */
  questionProperty: {
    type: String,
    default: 'title'
  },
  
  /**
   * Key name of object in items array for specifying content text of open question
   */
  answerProperty: {
    type: String,
    default: 'value'
  },
  
  /**
   * Key name of object in items array for specifying navigation tab name
   */
  tabName: {
    type: String,
    default: 'category'
  },
  
 /**
  * Color for hover and active tab/question
  * possible format: 'red', '#F00', 'rgba(255, 0, 0, 1)'
  */
  activeColor: {
    type: String,
    default: '#D50000'
  },
  
  /**
   * Color for borders
   */
  borderColor: {
    type: String,
    default: '#9E9E9E'
  },
  
  /**
   * Color for fonts
   */
  fontColor: {
    type: String,
    default: '#000000'
  }
  
}