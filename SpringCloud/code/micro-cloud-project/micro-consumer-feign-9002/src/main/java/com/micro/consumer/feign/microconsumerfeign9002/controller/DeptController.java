package com.micro.consumer.feign.microconsumerfeign9002.controller;

import com.micro.api.feign.microapifeign.dept.service.bean.Dept;
import com.micro.api.feign.microapifeign.dept.service.service.DeptService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class DeptController {

    @Autowired
    DeptService deptService;

    @RequestMapping(value = "/getdept", method = RequestMethod.GET)
    public List<Dept> getlist() {
        List<Dept> list = deptService.getList();
        return list;
    }
}
