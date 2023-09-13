
(cl:in-package :asdf)

(defsystem "tutorial_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "TutorialMsg" :depends-on ("_package_TutorialMsg"))
    (:file "_package_TutorialMsg" :depends-on ("_package"))
  ))