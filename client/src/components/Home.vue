<template>

<div>
 <v-carousel>
    <v-carousel-item
      v-for="(item,i) in items"
      :key="i"
      :src="item.src"
    ></v-carousel-item>
  </v-carousel>

      <v-carousel style="height: 100%">
        <v-carousel-item v-for="(slide, i) in slides" :src="slide.src" :key="i">
          <v-jumbotron dark>
            <v-container fill-height>
              <v-layout align-center>
                <v-flex>
                  <h3 class="display-3">{{ slide.title }}</h3>
                  <span class="subheading">{{ slide.text }}</span>
                </v-flex>
              </v-layout>
            </v-container>
          </v-jumbotron>
        </v-carousel-item>
      </v-carousel>
    </div>
</template>



<script>
import ima from '@/assets/WTC_1.png'
import ima2 from '@/assets/WTC_2.png'
import ima3 from '@/assets/WTC3.png'

  export default {
    data () {
      return {
        items: [
          {
            src: ima
            
          },
          {
            src: ima2
          },
          {
            src: ima3
          },
          {
            src: ima3
          }
        ]
      }
    }
  }
</script>