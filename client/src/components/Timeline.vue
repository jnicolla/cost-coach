

<template>
 <div>
   <center> <font color="blue"> <h1 class="md-display-3">Your Timeline</h1></font></center>
   <center><md-content class="md-accent"><h1 class="md-title">Total Treatment Cost:<br /><br />$8,500</h1></md-content>  <md-content class="md-primary"><h1 class="md-title">Cost Before OOP:<br /><br />$4,700</h1></md-content>  <md-content class="md-accent"><h1 class="md-title">OOP Reached Date:<br /><br />March 9th, 2019</h1></md-content> </center>
   <light-timeline :items='items'></light-timeline>


    </div>



</template>

<style lang="scss" scoped>

  .md-content 
  {
    width: 250px;
    height: 150px;
     display: inline-block;
    justify-content: center;
    align-items: center;
  }
  
</style>

<script>
const theme = 'blue';
export default {
  data () {
    return {
      items: [
        {
          tag: '2018-09-27',
          color: '#1baae6',
          content: 'Visit 1: Docotor Visit'
        },
        {
          tag: '2018-10-12',
          color: '#093af1',
          type: 'star',
          content: 'Visit 2: Chemotherapy Session'
        },
        {
          tag: '2018-11-15',
          type: 'circle', 
          color: '#1baae6', 
          htmlMode: true,
          content: `Visit 3: Routine Check-up`
        },
        {
          tag: '2018-09-27',
          color: '#1baae6',
          content: 'Visit 4: Docotor Visit'
        },
        {
          tag: '2018-10-12',
          color: '#093af1',
          type: 'star',
          content: 'Visit 5: Chemotherapy Session'
        },
        {
          tag: '2018-11-15',
          type: 'circle', 
          color: '#1baae6', 
          htmlMode: true,
          content: `Visit 6: Routine Check-up`
        },
        {
          tag: '2018-09-27',
          color: '#1baae6',
          content: 'Visit 7: Docotor Visit'
        },
        {
          tag: '2018-10-12',
          color: '#093af1',
          type: 'star',
          content: 'Visit 8: Chemotherapy Session'
        },
        {
          tag: '2018-11-15',
          type: 'circle', 
          color: '#1baae6', 
          htmlMode: true,
          content: `Visit 9: Routine Check-up`
        },
        {
          tag: '2018-09-27',
          color: '#1baae6',
          content: 'Visit 10: Docotor Visit'
        },
        {
          tag: '2018-10-12',
          color: '#093af1',
          type: 'star',
          content: 'Visit 11: Chemotherapy Session'
        },
        {
          tag: '2018-11-15',
          type: 'circle', 
          color: '#1baae6', 
          htmlMode: true,
          content: `Visit 12: Routine Check-up`
        }
      ]
    }
  }
}
  
</script>

