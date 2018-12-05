<template>
<div>
  <h4 id = "timelineTitleObj" class="display-1 font-weight-light grey--text text--darken-2">Cost Timeline</h4>
  <v-timeline dense>
    <v-timeline-item v-for="(event,index) in events"
      :key="index"
      color="#d65f36"
      :icon="event.icon"
      :small="index<events.length-1"
      :large="index==events.length-1"
      fill-dot
    >
      <div class="py-3 grey--text text--darken-2">
        <h5 v-if="index==events.length-1" class="title green--text text--darken-2 mb-2">Out of pocket maximum reached</h5>
        <h5 class="headline mb-3">
          {{ index+1 }}. Visit type: <span class="font-weight-bold">{{ event.visit }}</span>
        </h5>
        <div>
          <span v-if="index==events.length-1">At this stage, you will have reached your out-of-pocket maximum.</span>
          <span v-else>
            You will be approximately <span class="font-weight-bold">&#36;{{event.money}}</span> 
            away from reaching your out-of-pocket maximum.
          </span>
        </div>
      </div>
    </v-timeline-item>
  </v-timeline>
</div>
</template>


<script>

export default {
  name: "Timeline",
  props: ["data"],

  data() {
    return {
      events: []
    }
  },

  created() {
    for (var i=0; i<this.data.data.length; i++) {
      var info = this.data.data[i].split(",");
      var visit = info[1];
      var money = parseFloat(info[2]).toFixed(2);
      var icon = (i==this.data.data.length-1)? "star":"";
      this.events.push({
        visit: visit,
        money: money,
        icon: icon,
      });
    }
  }
}
</script>