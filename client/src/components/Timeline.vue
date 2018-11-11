<template>
<div>
  <h1>Your Road to Recovery</h1>
  <v-timeline>
    <v-timeline-item v-for="(event,index) in events" :key="event.id" color="primary" large>
      <span slot="opposite">{{event.date}}</span>
      <v-card class="elevation-2">
        <v-card-title class="headline" primary-title>{{event.visit}}</v-card-title>
        <v-card-text v-if="index==events.length"> At this stage, you have reached your out-of-pocket maximum</v-card-text>
        <v-card-text v-else>You will be approximately {{event.money}} away from reaching your out-of-pocket maximum.</v-card-text>
      </v-card>
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
    for (var i=0; i<this.data.events.length; i++) {
      var info = this.data.events[i].split(";");
      var visit = info[0];
      var date = info[1];
      var money = info[2];
      this.events.push({
        visit: visit,
        date: date,
        money: money
      });
    }
  }

}
</script>