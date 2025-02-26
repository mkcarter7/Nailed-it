from django.db import models  # Import base class from Django stdlib
from .tool import Tool
from .project import Project

class ProjectTool(models.Model):  #manytomany
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name="projecttool")
    #projecttool allows reverse look up from tool
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="toolproject")
    #toolproject allows reverse look up from project
