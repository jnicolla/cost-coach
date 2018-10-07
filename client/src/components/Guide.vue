<template>
<div>
    <center> <h1 class="md-display-3">Conversation Guideline</h1></center><center> <font color="md-accent">Welcome to your Timeline. Your Timeline will show you your expected expenses and costs.</font></center>
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
            title: 'How many times do I take my medicine?',
            value: '7 times a day',
            category: 'Treatment Questions'
          },
          {
            title: 'How many times do I take my medicine?',
            value: '7 times a day',
            category: 'Treatment Questions'
          },
          {
            title: 'How many times do I take my medicine?',
            value: '7 times a day',
            category: 'Treatment Questions'
          },
          {
            title: 'How many times do I take my medicine?',
            value: '7 times a day',
            category: 'Treatment Questions'
          },
          {
            title: 'How many times do I take my medicine?',
            value: '7 times a day',
            category: 'Treatment Questions'
          },
          {
            title: 'How do I contact my insurance company?',
            value: 'You can call them at: 999 999 9999',
            category: 'Finance Questions'
          },
          {
            title: 'Who is the FCC',
            value: 'Financial Cousling something',
            category: 'Finance Questions'
          }, 
           {
            title: 'Who is the FCC',
            value: 'Financial Cousling something',
            category: 'Finance Questions'
          },
           {
            title: 'Who is the FCC',
            value: 'Financial Cousling something',
            category: 'Finance Questions'
          },
           {
            title: 'Who is the FCC',
            value: 'Financial Cousling something',
            category: 'Finance Questions'
          },
           {
            title: 'Who is the FCC',
            value: 'Financial Cousling something',
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