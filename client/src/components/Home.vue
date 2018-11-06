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
import image1 from '@/assets/WTC1.png'
import image2 from '@/assets/WTC2.png'
import image3 from '@/assets/WTC3_v1.png'
import image4 from '@/assets/WTC4.png'

  export default {
    data () {
      return {
        items: [
          {
            src: image1
            
          },
          {
            src: image2
          },
          {
            src: image3
          },
          {
            src: image4
          }
        ]
      }
    }
  }
</script>