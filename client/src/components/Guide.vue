<template>
  <v-container fluid>
    <v-layout row justify-center>
      <v-flex xs12 lg10>
        <v-card raised>
        <!-- nested containers -->
          <v-container>
            <v-layout>
              <v-flex>
                <v-card-title class="display-3 font-weight-thin mx-3 mb-2 pb-0">
                  CostCoach Guide
                </v-card-title>
                <v-card-text class="grey--text text--darken-1 title mx-3 pb-0 mb-0 font-weight-light">
                  Select any questions you have below, click "Generate", 
                  and bring a printed copy of the generated file to your next doctor's appointment 
                  to have your questions answered.
                </v-card-text>
              </v-flex>
            </v-layout>
          </v-container>
        <!-- start second container -->
          <v-container grid-list-lg class="mx-4 mt-0 pt-0">
            <v-layout row wrap justify-start>
              <v-flex v-for="question in questions" :key="question.id" xs12 md6 lg4>
                <v-checkbox
                  :label="question.q"
                  :value="question.q"
                  color="#d65f36"
                  hide-details
                  v-model="question.checked"
                ></v-checkbox>
              </v-flex>
            </v-layout>
          </v-container>
        <!-- end second container -->

          <v-container>
            <v-layout>
              <v-flex>
                <v-card-actions class="mx-3">
                  <v-btn @click="genPDF" color="success">Generate</v-btn>
                </v-card-actions>
              </v-flex>
            </v-layout>
          </v-container>

        <!-- end nested containers -->
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import jsPDF from "jspdf"

export default {
  data() {
    return {
      questions:[
        {
          q:"If tomato is a fruit, is ketchup a smoothie?",
          checked:false
        },
        {q:"If a cyclops closes its eye, is it blinking or winking?", checked:false},
        {q:"If you succeed in an attempt to fail, have you succeeded or failed?", checked:false},
        {q:"What color does a Smurf turn when you choke it?", checked:false}
      ]
    }
  },

  computed: {
    checkedQs() {
      return this.questions.filter((question) => {
        return question.checked;
      }).map((question) => {
        return question.q;
      });
    }
  },

  methods: {
    genPDF() {
      var doc = new jsPDF();
      doc.text(30,30,this.checkedQs);
      doc.save("Questions.pdf");
    }
  }
}
</script>