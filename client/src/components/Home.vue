<template>
  <v-content>
    <v-container fluid>
      <v-layout justify-center row fill-height wrap>
        <v-flex xs11 md10 lg9 class="mb-3">
          <!-- sets max width -->
          <!-- grid begins here -->
          <v-container fluid grid-list-lg>
            <v-layout justify-center row fill-height wrap>
              
              
              <v-flex xs12>
                <v-card hover>
                  <v-container>
                    <v-layout>
                      <v-flex>
                        <div class="mx-4">
                          <h3 class="display-3 pb-2 font-weight-thin">Welcome to CostCoach</h3>

                          <span class="subheading">
                            CostCoach is the world's first application that can calculate your cancer treatment costs. 
                            You only need three pieces of information to use it: your insurance plan, diagnosis, and medications.
                          </span>
                        </div>

                        <v-divider class="my-3 px-4"></v-divider>

                        <div class="mx-4">
                          <div class="title mb-3 font-weight-light">Click the button below and get started</div>

                          <v-btn
                            class="mx-0"
                            color="primary"
                            large
                            to="/calculator"
                          >
                            <span class="white--text font-weight-bold">Calculator</span>
                          </v-btn>
                        </div>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-card>
              </v-flex>

              <v-flex xs12 md6>
                <v-card hover>
                  <v-container>
                    <v-layout>
                      <v-flex>
                        <div class="mx-4">
                          <h3 class="display-1 pb-2 font-weight-light">Fighting the Stigma</h3>

                          <span class="subheading">
                            Having a conversation with your health care provider about finances can be challenging. To make 
                            this conversation easier, a list of common questions have been assembled in our Guide.
                          </span>
                        </div>

                        <v-divider class="my-3 px-4"></v-divider>

                        <div class="mx-4">
                          <div class="title mb-3 font-weight-light">Find your questions here</div>

                          <v-btn
                            class="mx-0"
                            color="primary"
                            large
                            to="/guide"
                            outline
                          >
                            <span class="font-weight-bold">Guide</span>
                          </v-btn>
                        </div>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-card>
              </v-flex>


              <v-flex xs12 md6>
                <v-card hover>
                  <v-container>
                    <v-layout>
                      <v-flex>
                        <div class="mx-4">
                          <h3 class="display-1 pb-2 font-weight-light">Did you know?</h3>

                          <p class="subheading mb-4">
                            The Agency for Healthcare Research and Quality (AHRQ) estimates that the direct medical costs 
                            (total of all health care costs) for cancer in the US in 2015 were 
                            <span class="font-weight-bold">$80.2 billion</span>.
                          </p>

                          <p class="subheading mb-2">
                            <span class="font-weight-bold">52 percent</span> of patients desire a cost discussion with their oncologist.
                          </p>

                          <p class="subheading mb-2">
                            <span class="font-weight-bold">57 percent</span> of patients reported lower treatment costs due to a discussion.
                          </p>

                          <p class="subheading">
                            <span class="font-weight-bold">19 percent</span> of patients actually have a cost discussion.
                          </p>
                        </div>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-card>
              </v-flex>

            
          
            </v-layout>
          </v-container>
        
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
export default {
  name: "Home"
}
</script>