<template>
    <div>
        <slot></slot>
        <div class="intro-form-counter-block" v-if="counter < 150">
            <img src="/static/images/symbols-counter/quarter_segment-circle-icon.svg"
                alt="quarter segment circle icon" />
            <span>Подробное интро будет полезнее другим членам Клуба для знакомства с вами</span>
        </div>
        <div class="intro-form-counter-block" v-if="counter >= 150 && counter < 300">
            <img src="/static/images/symbols-counter/half_segment-circle-icon.svg" alt="half segment circle icon" />
            <span>Дополните немного интро, оно станет ещё качественнее</span>
        </div>
        <div class="intro-form-counter-block" v-if="counter >= 300">
            <img src="/static/images/symbols-counter/full-circle-icon.svg" alt="full circle icon" />
            <span>Отлично, такое интро очень поможет нетворкингу с коллегами по Клубу</span>
        </div>
        <div class="intro-form-counter-display">
            {{ counter !== null ? counter : "-" }}
            <span>&nbsp;&#47;&nbsp;{{ minLength }}</span>
        </div>
    </div>
</template>

<script>
import { throttle } from "../common/utils.js";

export default {
    name: "InputLengthCounter",
    props: {
        minLength: {
            type: Number,
            default: 0,
        },
        delay: {
            type: Number,
            default: 300,
        },
        element: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            counter: null,
            $target: null,
        };
    },
    mounted() {
        this.$target = document.querySelector(this.element);
        if (!this.$target) {
            return console.warn(`${this.element} is not found.`);
        }

        if (!(this.$target instanceof HTMLTextAreaElement) && !(this.$target instanceof HTMLInputElement)) {
            return console.warn(`${this.element} is not an input element.`);
        }

        this.counter = this.$target.value.length;

        this.throttledCounterHandler = throttle((e) => {
            this.counter = e.target.value.length;
        }, this.delay);

        this.$target.addEventListener("keyup", this.throttledCounterHandler);
    },
    beforeDestroy() {
        if (this.$target) {
            this.$target.removeEventListener("keyup", this.throttledCounterHandler);
        }
    },
};

</script>
