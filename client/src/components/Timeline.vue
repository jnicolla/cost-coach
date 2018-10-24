

<template>
 <div>
   <center> <font color="blue"> <h1 class="md-display-3">Your Timeline</h1></font></center>
   <center><md-content class="md-accent"><h1 class="md-title">Total Treatment Cost:<br /><br />$8,500</h1></md-content>  <md-content class="md-primary"><h1 class="md-title">Cost Before OOP:<br /><br />$4,700</h1></md-content>  <md-content class="md-accent"><h1 class="md-title">OOP Reached Date:<br /><br />October 12th, 2018</h1></md-content> </center>
   <light-timeline :items='items'></light-timeline>

<div class="phone-viewport">
      <center> <font color="white">.</font></center>
 <center> <font color="white">.</font></center>
 <center> <font color="white">.</font></center>
 <center> <font color="white">.</font></center>

 
 <md-bottom-bar class="md-primary" md-type="shift">
  <center><font color="white">CostCoach © 2018</font></center>

 <md-bottom-bar-item id="" md-label="" md-icon=""></md-bottom-bar-item> 


                                                          
                                           

      </md-bottom-bar>
    </div>
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
const theme = 'Orange';
export default {
  data () {
    return {
      items: [
        {
          tag: '2018-09-27',
          color: '#232859',
          content: 'Visit 1: Docotor Visit   - $50'
        },
        {
          tag: '2018-10-12',
          type: 'circle', 
          color: '#d65f36',
          content: 'Visit 2: Chemotherapy Session -$150'
        },
        {
          tag: '2018-11-15',
          type: 'circle', 
          color: '#d65f36', 
          htmlMode: true,
          content: `Visit 3: Routine Check-up - $75`
        },
        {
          tag: '2018-09-27',
          color: '#d65f36',
          content: 'Visit 4: Docotor Visit - $75'
        },
        {
          tag: '2018-10-12',
          type: 'circle', 
          color: '#232859',
          content: 'Visit 5: Chemotherapy Session - $175'
        },
        {
          tag: '2018-11-15',
          type: 'circle', 
          color: '#232859', 
          htmlMode: true,
          content: `Visit 6: Routine Check-up - $275`
        },
        {
          tag: '2018-09-27',
          color: '#232859',
          content: 'Visit 7: Docotor Visit - $25'
        },
        {
          tag: '2018-10-12',
          color: '#d65f36',
          type: 'star',
          content: 'Visit 8: Chemotherapy Session - $475'
        },
        {
          tag: '2018-11-15',
          type: 'circle', 
          color: '#232859', 
          htmlMode: true,
          content: `Visit 9: Routine Check-up - $15`
        },
        {
          tag: '2018-09-27',
          color: '#232859',
          content: 'Visit 10: Docotor Visit - $45'
        },
        {
          tag: '2018-10-12',
          type: 'circle', 
          color: '#232859',
          content: 'Visit 11: Chemotherapy Session - $175'
        },
        {
          tag: '2018-11-15',
          type: 'circle', 
          color: '#232859', 
          htmlMode: true,
          content: `Visit 12: Routine Check-up - $75`
        }
      ]
    }
  }
}
  
</script>

