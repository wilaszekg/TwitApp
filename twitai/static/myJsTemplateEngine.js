var MyEngine = {
    compile: function (template) {
        return {
            render: function (context) {
                return template.replace(/##(\w+)/g, function (match, p1) {
                    return context[p1];
                });
            }
        };
    }
};