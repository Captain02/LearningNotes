package com.micro.hystrix.microproviderhystrix8003.dept.controller;

import com.entity.Dept;
import com.micro.hystrix.microproviderhystrix8003.dept.service.DeptService;
import com.netflix.hystrix.contrib.javanica.annotation.HystrixCommand;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class DeptController {

    @Autowired
    DeptService deptService;

    @GetMapping("/getlist/{id}")
    @HystrixCommand(fallbackMethod = "processHystrix_Get")
    public Dept getList(@PathVariable("id") Integer id) {
        List<Dept> list = deptService.list();
        Dept dept = list.get(id);
        if (dept == null) {
            throw new RuntimeException("该ID：" + id + "没有没有对应的信息");
        }
        return dept;
    }

    public Dept processHystrix_Get(@PathVariable("id") Integer id) {
        Dept dept = new Dept();
        dept.setId(10);
        dept.setDeptname("没有没有对应的信息--@HystrixCommand");
        dept.setDb("0");
        dept.setDescs("没有没有对应的信息--@HystrixCommand");
        return dept;
    }

}
