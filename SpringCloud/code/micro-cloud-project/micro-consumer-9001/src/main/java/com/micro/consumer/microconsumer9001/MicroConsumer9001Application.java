package com.micro.consumer.microconsumer9001;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;

@SpringBootApplication
@EnableEurekaClient
public class MicroConsumer9001Application {

	public static void main(String[] args) {
		SpringApplication.run(MicroConsumer9001Application.class, args);
	}

}
