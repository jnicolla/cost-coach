<template>
  <v-container fluid>
    <v-layout row justify-center>
      <v-flex xs12 lg10>
        <v-card raised>
        <!-- nested containers -->
          <v-container>
            <v-layout>
              <v-flex>
                <v-card-title id = "Title" class="display-3 font-weight-thin mx-3 mb-2 pb-0">
                  Conversational Guide
                </v-card-title>
                <v-card-text id = "Main_Body" class="grey--text text--darken-1 title mx-3 pb-0 mb-0 font-weight-light">
                  <p class="pb-2">The purpose of this guide is to help structure a conversation about the costs of treatment 
                  with your healthcare professional.</p>
                  
                  <p>To use it, select any questions you have below and click "Generate".
                  This will generate a file containing your selected questions, which you can print and bring to your next doctor's
                  appointment.</p>
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
                  <v-btn id = "PDFG" @click="genPDF" color="success">Generate</v-btn>
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
        {q:"Is my current insurance plan right for me?", checked:false},
        {q:"What resources are available to help me with financial planning?", checked:false},
        {q:"What if I can't afford a particular visit/treatment?", checked:false},
        {q:"Are my drugs covered by my insurance plan?", checked:false}
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